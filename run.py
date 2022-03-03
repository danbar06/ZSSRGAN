import os
from argparse import Namespace

from Utils import configs
from train import train
from main import create_params

INPUT_IMAGE_PATH = '../single_train'
OUTPUT_IMAGE_PATH = '../single_train_result'
DISC_LOSS_RATIO_LIST = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def run():
    for disc_loss_ratio in DISC_LOSS_RATIO_LIST:
        args = Namespace(DL=True,
                         UK=True,
                         X4=True,
                         disc_loss_ratio=disc_loss_ratio,
                         input_dir=INPUT_IMAGE_PATH,
                         noise_scale=1.0,
                         output_dir=OUTPUT_IMAGE_PATH,
                         real=True,
                         type='fixed')
        for filename in os.listdir(os.path.abspath(args.input_dir)):
            configs.parse(create_params(filename, args))
            train()


if __name__ == "__main__":
    run()
