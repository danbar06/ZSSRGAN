import matplotlib.image as img
from ZSSRforKernelGAN.zssr_configs import Config
from ZSSRforKernelGAN.zssr_utils import *
from ZSSRforKernelGAN_pytorch import ZSSR_network
import torch
from torch import nn
import tensorflow as tf
import tqdm

class ZSSR:
    # Basic current state variables initialization / declaration
    kernel = None
    learning_rate = None
    hr_father = None
    lr_son = None
    sr = None
    sf = None
    gt_per_sf = None
    final_sr = None
    hr_fathers_sources = []

    # Output variables initialization / declaration
    reconstruct_output = None
    train_output = None
    output_shape = None

    # Counters and logs initialization
    iter = 0
    base_sf = 1.0
    base_ind = 0
    sf_ind = 0
    mse = []
    mse_rec = []
    interp_rec_mse = []
    interp_mse = []
    mse_steps = []
    loss = []
    learning_rate_change_iter_nums = []
    fig = None

    # Network tensors (all tensors end with _t to distinguish)
    learning_rate_t = None
    lr_son_t = None
    hr_father_t = None
    filters_t = None
    layers_t = None
    net_output_t = None
    loss_t = None
    loss_map_t = None
    train_op = None
    init_op = None

    # Parameters related to plotting and graphics
    plots = None
    loss_plot_space = None
    lr_son_image_space = None
    hr_father_image_space = None
    out_image_space = None

    # A map representing the gradient magnitude of the image at every crop
    prob_map = None
    cropped_loss_map = None
    avg_grad = 1
    loss_map = []
    loss_map_sources = []

    # Tensorflow graph default
    sess = None

    def __init__(self, input_img_path, scale_factor=2, kernels=None, is_real_img=False, noise_scale=1.):
        # Save input image path
        self.input_img_path = input_img_path
        # Acquire meta parameters configuration from configuration class as a class variable
        self.conf = Config(scale_factor, is_real_img, noise_scale)
        # Read input image
        self.input = img.imread(input_img_path)
        # Discard the alpha channel from images
        if self.input.shape[-1] == 4:
            self.input = img.imread(input_img_path)[:, :, :3]
        # For gray-scale images - add a 3rd dimension to fit the network
        elif len(self.input.shape) == 2:
            self.input = np.expand_dims(self.input, -1)
        self.input = self.input / 255. if self.input.dtype == 'uint8' else self.input
        self.gt = None
        # Shift kernel to avoid misalignment
        self.kernels = []
        set_kernels(kernels)

        # Check if cuda is available
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # Build network computational graph
        # self.build_network(self.conf) NOT ALL IS IMPLEMENTED YET
        self.network = ZSSR_network.ZSSR_network(self.conf).to(self.device)

        # Initialize network weights and meta parameters
        self.weights_initiator = ZSSR_network.weights_init_ZSSR(self.conf)
        self.network.apply(self.weights_initiator)
        self.init_sess()

        # The first hr father source is the input (source goes through augmentation to become a father)
        # Later on, if we use gradual sr increments, results for intermediate scales will be added as sources.
        self.hr_fathers_sources = [self.input]

        # Create a loss map reflecting the weights per pixel of the image
        self.loss_map = create_loss_map(im=self.input) if self.conf.grad_based_loss_map else np.ones_like(self.input)

        # define loss function
        self.criterion = Weighted_L1Loss()

        # loss maps that correspond to the father sources array
        self.loss_map_sources = [self.loss_map]

        # Optimizers
        self.optimizer = torch.optim.Adam(self.network.parameters(), lr=self.learning_rate, betas=(0.9, 0.999))

    def set_kernels(self, kernels):
        if kernels is not None:
            self.kernels = [kernel_shift(kernel, sf) for kernel, sf in zip(kernels, self.conf.scale_factors)]
        else:
            self.kernels = [self.conf.downscale_method] * len(self.conf.scale_factors)

    def init_sess(self):
        # Initialize all counters etc
        self.loss = [None] * self.conf.max_iters
        self.mse, self.mse_rec, self.interp_mse, self.interp_rec_mse, self.mse_steps = [], [], [], [], []
        self.iter = 0
        self.learning_rate = self.conf.learning_rate
        self.learning_rate_change_iter_nums = [0]

    def learning_rate_policy(self):
        # fit linear curve and check slope to determine whether to do nothing, reduce learning rate or finish
        if (not (1 + self.iter) % self.conf.learning_rate_policy_check_every
                and self.iter - self.learning_rate_change_iter_nums[-1] > self.conf.min_iters):
            # noinspection PyTupleAssignmentBalance
            [slope, _], [[var, _], _] = np.polyfit(self.mse_steps[-int(self.conf.learning_rate_slope_range /
                                                                       self.conf.run_test_every):],
                                                   self.mse_rec[-int(self.conf.learning_rate_slope_range /
                                                                     self.conf.run_test_every):],
                                                   1, cov=True)

            # We take the the standard deviation as a measure
            std = np.sqrt(var)

            # Determine learning rate maintaining or reduction by the ration between slope and noise
            if -self.conf.learning_rate_change_ratio * slope < std:
                self.learning_rate /= 10

                # Keep track of learning rate changes for plotting purposes
                self.learning_rate_change_iter_nums.append(self.iter)
                return True
        return False

    def train(self):
        # main training loop
        for self.iter in tqdm.tqdm(range(self.conf.max_iters), ncols=60):
            # Use augmentation from original input image to create current father.
            # If other scale factors were applied before, their result is also used (hr_fathers_in)
            # crop_center = choose_center_of_crop(self.prob_map) if self.conf.choose_varying_crop else None
            crop_center = None

            self.hr_father, self.cropped_loss_map = \
                random_augment(ims=self.hr_fathers_sources,
                               base_scales=[1.0] + self.conf.scale_factors,
                               leave_as_is_probability=self.conf.augment_leave_as_is_probability,
                               no_interpolate_probability=self.conf.augment_no_interpolate_probability,
                               min_scale=self.conf.augment_min_scale,
                               max_scale=([1.0] + self.conf.scale_factors)[len(self.hr_fathers_sources) - 1],
                               allow_rotation=self.conf.augment_allow_rotation,
                               scale_diff_sigma=self.conf.augment_scale_diff_sigma,
                               shear_sigma=self.conf.augment_shear_sigma,
                               crop_size=self.conf.crop_size,
                               allow_scale_in_no_interp=self.conf.allow_scale_in_no_interp,
                               crop_center=crop_center,
                               loss_map_sources=self.loss_map_sources)

            # Get lr-son from hr-father
            self.lr_son = self.father_to_son(self.hr_father)
            # run network forward and back propagation, one iteration (This is the heart of the training)
            # Zeroize gradients
            self.optimizer.zero_grad()
            # ZSSR forward pass
            pred = self.network.forward(self.lr_son)
            # Convert target to torch
            hr_father = torch.tensor(self.hr_father, requires_grad=True)
            cropped_loss_map = torch.tensor(self.cropped_loss_map, requires_grad=False)
            # Add batch dimension
            hr_father = torch.unsqueeze(hr_father, dim=0)
            cropped_loss_map = torch.unsqueeze(cropped_loss_map, dim=0)
            # Final loss (Weighted (cropped_loss_map) L1 loss between label and output layer)
            loss = self.criterion(pred, hr_father, cropped_loss_map)
            # Initiate backprop
            loss.backward()
            self.optimizer.step()

            # NEED TO CHECK BLOW LINES
            # Run network
            # _, self.loss[self.iter], train_output = self.sess.run([self.train_op, self.loss_t, self.net_output_t],
            #                                                       feed_dict)
            # return np.clip(np.squeeze(train_output), 0, 1)


            # Test network
            if self.conf.run_test and (not self.iter % self.conf.run_test_every):
                self.quick_test()

            # Consider changing learning rate or stop according to iteration number and losses slope
            if self.learning_rate_policy():
                for param_group in self.optimizer.param_groups:
                    param_group['lr'] = self.learning_rate

            # stop when minimum learning rate was passed
            if self.learning_rate < self.conf.min_learning_rate:
                break

    def father_to_son(self, hr_father):
        # Create son out of the father by downscaling and if indicated adding noise
        lr_son = imresize(hr_father, 1.0 / self.sf, kernel=self.kernel)
        return np.clip(lr_son + np.random.randn(*lr_son.shape) * self.conf.noise_std, 0, 1)