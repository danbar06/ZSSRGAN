# Zero Shot Super Resolution using KernelGAN estimated Kernel and Discriminator
### Dan Bar, Neta Shaul, Yeari Vigder

<br/>
<br/>

## Abstract
The project considers the problem of 'Super Resolution' (SR).
It offers an image-specific CNN solution that is based on [ZSSR](https://www.wisdom.weizmann.ac.il/~vision/zssr/) but combines more work that has been done, see  [KernelGAN](https://www.wisdom.weizmann.ac.il/~vision/kernelgan/), [SinGAN](https://github.com/tamarott/SinGAN).
In KernelGAN only the generator of the network was used as a downscale kernel to improve the ZSSR result.
However, in SinGAN, it was shown that adversarial training could be used to give state of the art (SOTA) results for SR,
but long times are required to train the network.
We propose to also utilize the discriminator of KernelGAN in order to improve the result for SR within shorter times.

[Results](data.md)
