
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0014)about:internet -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <title>"Zero Shot" Super-Resolution using Deep Internal Learning</title>
    <link rel="stylesheet" type="text/css" href="./main.css" />

    <script type="text/JavaScript">
<!--
function MM_preloadImages() { //v3.0
 var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
  var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
  if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_swapImgRestore() { //v3.0
 var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_findObj(n, d) { //v4.01
 var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
  d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
 if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
 for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
 if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
 var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
 if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}
//-->
    </script>

</head>
<!-- Weizmann header -->
<br />
<div id="weizmann-header">
<img class="logo" src="./figs/logo_green2.gif" alt="Logo" />
<div class="logo_text">
  <p>
    <a class="logo_link" href="http://www.weizmann.ac.il" title="Visit the Weizmann Institute Homepage">The Weizmann Institute of Science</a><br />
    <a class="logo_link" href="http://www.wisdom.weizmann.ac.il" title="Visit Faculty of Math &amp; Computer Science Homepage">Faculty of Mathematics and Computer Science</a><br />
    <a class="logo_link" href="http://www.wisdom.weizmann.ac.il/~vision/" title="Visit Computer Vision Lab Homepage">Computer Vision Lab</a><br />
  </p>
</div> <!-- logo_text -->
<hr class="logo_hr" />
<br />
</div> <!-- header -->
<!-- weizmann-header -->
    <blockquote>
    <h1>
        "Zero Shot" Super-Resolution using Deep Internal Learning
    </h1>
    
    <center>
    <a href="http://www.wisdom.weizmann.ac.il/~/assafsho/">Assaf Shocher</a>,
    <a href="http://www.cohennadav.com/">Nadav Cohen</a>,
    <a href="http://www.wisdom.weizmann.ac.il/~irani">Michal Irani</a>
    </center>
<br />


<body id="top-of-page">

    <center>
    This webpage presents the paper "Zero-Shot Super-Resolution using Deep Internal Learning" (CVPR 2018).<br />
    [<a href="http://www.weizmann.ac.il/math/irani/sites/math.irani/files/uploads/zssr_cameraready.pdf">Paper PDF</a>]
	[<a href="./cite_zssr.bib">bibtex</a>]
	[<a href="https://github.com/assafshocher/ZSSR">Code</a>]<br />
    </center>

    <br />
	</blockquote>
		<hr />
    <br />

    <blockquote>
    <h2>Abstract</h2>
Deep Learning has led to a dramatic leap in SuperResolution
(SR) performance in the past few years. However,
being supervised, these SR methods are restricted to
specific training data, where the acquisition of the lowresolution
(LR) images from their high-resolution (HR)
counterparts is predetermined (e.g., bicubic downscaling),
without any distracting artifacts (e.g., sensor noise, image
compression, non-ideal PSF, etc). Real LR images, however,
rarely obey these restrictions, resulting in poor SR results
by SotA (State of the Art) methods. In this paper we introduce
"Zero-Shot" SR, which exploits the power of Deep
Learning, but does not rely on prior training. We exploit
the internal recurrence of information inside a single image,
and train a small image-specific CNN at test time, on
examples extracted solely from the input image itself. As
such, it can adapt itself to different settings per image. This
allows to perform SR of real old photos, noisy images, biological
data, and other images where the acquisition process
is unknown or non-ideal. On such images, our method
outperforms SotA CNN-based SR methods, as well as previous
unsupervised SR methods. To the best of our knowledge,
this is the first unsupervised CNN-based SR method.
   </blockquote>
     <br />
		
		<br />	<hr /><br />
        <h1>Supplementary Material</h1>

    <blockquote>
        <h2>
            This file contains:
            <br />
            1. <a href="#real" title="Real photos experiment.">SR of Real photos experiment.</a><br />
            2. <a href="#rand_ker" title="Random kernel experiment.">SR under `non-ideal' downscaling kernels (The random kernel experiment)</a><br />
			3. <a href="#rand_deg" title="Random degradation experiment.">SR of poor-quality LR images (The random degradation experiment)</a><br />
			4. <a href="#additional" title="Remaining images from the paper figures.">Remaining images from the paper figures</a><br />

            <br />
            <br />
            <font color="red" size="6">To switch between images please use the colored buttons on the right.</font>
            <br />
        </h2>
    </blockquote>
	<hr />
	Relevant references: <br/>
	<b>[12]</b> B. Lim, S. Son, H. Kim, S. Nah, and K. M. Lee. <b><i>Enhanced deep residual networks for single image super-resolution.</b></i> In The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, July 2017.<br/>
	<b>[14]</b> T. Michaeli and M. Irani. <b><i>Nonparametric blind superresolution.</b></i> In International Conference on Computer Vision (ICCV), 2013. <br/>
	<hr />
	</center>
	<a id="real"><span style="font-weight: bold; font-size: 1.5em; color:red; background-color: #cccccc;">1. Real Low-res images </span> <span style="font-size: 1.5em; color:red;">(No ground truth) </a></h2><font size="5">
	<ul>
	<li>In REAL images taken under `non-ideal' conditions, SotA SR (e.g., EDSR [12]) is often only marginally better than bicubic interpolation.</li>
	<li>ZSSR can handle such non-ideal cases.</li></font>
        <hr />
 		<blockquote>
        <center>
		<span style="font-weight: bold; font-size: 1.5em; "><u>Historic image: Check-point Charlie (end of World-War II) - SR x2 </u></span><br/>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
					
					          <font size="5"><font size="5"><u><b id='method_001'>Bi-Cubic Interpolation</b><br/></font></font>
                        <img src="./real/img_001_SRF_2_BICUBIC.png" alt="High Resolution Image"/ id="001_real">
                    </td>
                    <td valign="top">
                        <font size="5">Input LR Image</font>
                        <br />
                        <img src="./real/img_001_SRF_2_LR.png" border="none" alt="Input image" />
                        <br />
                        <p>
                            &nbsp;
                        </p>
                        <br />
                        <button type="button" class="bic" id="001_real_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('001_real_edsr').style.fontWeight='normal';
                          document.getElementById('001_real_zssr').style.fontWeight='normal';
                          MM_swapImage('001_real','','./real/img_001_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_001').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="001_real_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('001_real_bicubic').style.fontWeight='normal';
                          document.getElementById('001_real_zssr').style.fontWeight='normal';
                          MM_swapImage('001_real','','./real/img_001_SRF_2_EDSR.png',1);
						  document.getElementById('method_001').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="001_real_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('001_real_bicubic').style.fontWeight='normal';
                          document.getElementById('001_real_edsr').style.fontWeight='normal';
                          MM_swapImage('001_real','','./real/img_001_SRF_2_ZSSR.png',1);
						  document.getElementById('method_001').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
	 		<blockquote>
        <center>
		<span style="font-weight: bold; font-size: 1.5em; "><u>Historic image: JFK funeral - SR x2  </u></span><br/>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
					
					          <font size="5"><u><b id='method_005'>Bi-Cubic Interpolation</b><br/></font>
                        <img src="./real/img_005_SRF_2_BICUBIC.png" alt="High Resolution Image"/ id="005_real">
                    </td>
                    <td valign="top">
                        <font size="5">Input LR Image</font>
                        <br />
                        <img src="./real/img_005_SRF_2_LR.png" border="none" alt="Input image" />
                        <br />
                        <p>
                            &nbsp;
                        </p>
                        <br />
                        <button type="button" class="bic" id="005_real_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('005_real_edsr').style.fontWeight='normal';
                          document.getElementById('005_real_zssr').style.fontWeight='normal';
                          MM_swapImage('005_real','','./real/img_005_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_005').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="005_real_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('005_real_bicubic').style.fontWeight='normal';
                          document.getElementById('005_real_zssr').style.fontWeight='normal';
                          MM_swapImage('005_real','','./real/img_005_SRF_2_EDSR.png',1);
						  document.getElementById('method_005').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="005_real_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('005_real_bicubic').style.fontWeight='normal';
                          document.getElementById('005_real_edsr').style.fontWeight='normal';
                          MM_swapImage('005_real','','./real/img_005_SRF_2_ZSSR.png',1);
						  document.getElementById('method_005').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
 		<blockquote>
        <center>
            <table style="width:20%">
			<span style="font-weight: bold; font-size: 1.5em; "><u>Historic image: Abraham Lincoln photograph - SR x2</u></span><br/>
                <tr>
                    <td rowspan="1" width="20%" valign="top">
					
					          <font size="5"><u><b id='method_002'>Bi-Cubic Interpolation</b><br/></font>
                        <img src="./real/img_002_SRF_2_BICUBIC.png" alt="High Resolution Image"/ id="002_real">
                    </td>
                    <td valign="top">
                        <font size="5">Input LR Image</font>
                        <br />
                        <img src="./real/img_002_SRF_2_LR.png" border="none" alt="Input image" />
                        <br />
                        <p>
                            &nbsp;
                        </p>
                        <br />
                        <button type="button" class="bic" id="002_real_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('002_real_edsr').style.fontWeight='normal';
                          document.getElementById('002_real_zssr').style.fontWeight='normal';
                          MM_swapImage('002_real','','./real/img_002_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_002').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="002_real_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('002_real_bicubic').style.fontWeight='normal';
                          document.getElementById('002_real_zssr').style.fontWeight='normal';
                          MM_swapImage('002_real','','./real/img_002_SRF_2_EDSR.png',1);
						  document.getElementById('method_002').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="002_real_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('002_real_bicubic').style.fontWeight='normal';
                          document.getElementById('002_real_edsr').style.fontWeight='normal';
                          MM_swapImage('002_real','','./real/img_002_SRF_2_ZSSR.png',1);
						  document.getElementById('method_002').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
 		<blockquote>
        <center>
		<span style="font-weight: bold; font-size: 1.5em; "><u>iPhone image - SR x3</u></span><br/>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
					
					          <font size="5"><u><b id='method_003'>Bi-Cubic Interpolation</b><br/></font>
                        <img src="./real/img_003_SRF_2_BICUBIC.png" alt="High Resolution Image"/ id="003_real">
                    </td>
                    <td valign="top">
                        <font size="5">Input LR Image</font>
                        <br />
                        <img src="./real/img_003_SRF_2_LR.png" border="none" alt="Input image" />
                        <br />
                        <p>
                            &nbsp;
                        </p>
                        <br />
                        <button type="button" class="bic" id="003_real_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('003_real_edsr').style.fontWeight='normal';
                          document.getElementById('003_real_zssr').style.fontWeight='normal';
                          MM_swapImage('003_real','','./real/img_003_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_003').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="003_real_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('003_real_bicubic').style.fontWeight='normal';
                          document.getElementById('003_real_zssr').style.fontWeight='normal';
                          MM_swapImage('003_real','','./real/img_003_SRF_2_EDSR.png',1);
						  document.getElementById('method_003').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="003_real_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('003_real_bicubic').style.fontWeight='normal';
                          document.getElementById('003_real_edsr').style.fontWeight='normal';
                          MM_swapImage('003_real','','./real/img_003_SRF_2_ZSSR.png',1);
						  document.getElementById('method_003').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
 		<blockquote>
        <center>
		<span style="font-weight: bold; font-size: 1.5em; "><u>Outdoor image downloaded from the Internet - SR x2 </u></span><br/>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
					
					          <font size="5"><u><b id='method_004'>Bi-Cubic Interpolation</b><br/></font>
                        <img src="./real/img_004_SRF_2_BICUBIC.png" alt="High Resolution Image"/ id="004_real">
                    </td>
                    <td valign="top">
                        <font size="5">Input LR Image</font>
                        <br />
                        <img src="./real/img_004_SRF_2_LR.png" border="none" alt="Input image" />
                        <br />
                        <p>
                            &nbsp;
                        </p>
                        <br />
                        <button type="button" class="bic" id="004_real_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('004_real_edsr').style.fontWeight='normal';
                          document.getElementById('004_real_zssr').style.fontWeight='normal';
                          MM_swapImage('004_real','','./real/img_004_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_004').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="004_real_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('004_real_bicubic').style.fontWeight='normal';
                          document.getElementById('004_real_zssr').style.fontWeight='normal';
                          MM_swapImage('004_real','','./real/img_004_SRF_2_EDSR.png',1);
						  document.getElementById('method_004').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="004_real_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('004_real_bicubic').style.fontWeight='normal';
                          document.getElementById('004_real_edsr').style.fontWeight='normal';
                          MM_swapImage('004_real','','./real/img_004_SRF_2_ZSSR.png',1);
						  document.getElementById('method_004').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>

	    <hr /></center>
	<a id="rand_ker"><span style="font-weight: bold; font-size: 1.5em; color:red; background-color: #cccccc;">2. SR under `non-ideal' downscaling kernels </span><span style="font-size: 1.5em; color:red;"> (The random kernel experiment)</span> </a><br/> <font size="5">
	        <ul>
<li>	LR images were generated using <b>"non-ideal"</b> (non-bicubic), but realistic, downscaling kernels (see Sec. 4.2 in the paper for more details). Each image was downscaled by a <b>different</b> random kernel (which is unknown to the SR algorithm). </li>
<li>         We used the method of [14] to <b>estimate the downscaling kernel directly from the test image</b>, and fed it to our image-specific network ZSSR.</li>
<li>         Note that SotA SR methods cannot benefit from knowing the downscaling kernel of a specific LR image at test time, since they were trained and optimized for a different (fixed) kernel - usually bicubic). </li>
<li>         In such `non-ideal' (but realistic) cases, SotA SR (e.g., EDSR [12]) is <b>often only marginally better than bicubic interpolation.</b></li>
<li>         ZSSR can handle such non-ideal cases.</li></font>
</ul>
<span style="font-weight: bold; font-size: 1.7em;"> Below we show a few sample images. Extensive empirical evaluation on the full dataset of 100 images can be found in the paper.</span>
        <hr />
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_007_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_007_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_007'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_007'>26.74 / 0.7817</b>
                        <img src="./rand_kernel/img_007_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="007_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_007_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="007_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('007_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('007_rand_ker','','./rand_kernel/img_007_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_007').innerHTML = '26.74 / 0.7817';
						  document.getElementById('method_007').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="007_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('007_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('007_rand_ker','','./rand_kernel/img_007_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_007').innerHTML = '27.87 / 0.8324';
						  document.getElementById('method_007').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="007_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('007_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('007_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('007_rand_ker','','./rand_kernel/img_007_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_007').innerHTML = '28.17 / 0.8424';
						  document.getElementById('method_007').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="007_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('007_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('007_rand_ker','','./rand_kernel/img_007_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_007').innerHTML = '30.23 / 0.9045';
						  document.getElementById('method_007').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="007_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('007_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('007_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('007_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('007_rand_ker','','./rand_kernel/img_007_SRF_2_HR.png',1);
						  document.getElementById('psnr_007').innerHTML = '&infin; / 1';
						  document.getElementById('method_007').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>

		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_016_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_016_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_016'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_016'>22.88 / 0.6608</b>
                        <img src="./rand_kernel/img_016_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="016_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_016_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="016_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('016_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('016_rand_ker','','./rand_kernel/img_016_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_016').innerHTML = '22.88 / 0.6608';
						  document.getElementById('method_016').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="016_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('016_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('016_rand_ker','','./rand_kernel/img_016_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_016').innerHTML = '23.22 / 0.6839';
						  document.getElementById('method_016').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="016_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('016_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('016_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('016_rand_ker','','./rand_kernel/img_016_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_016').innerHTML = '24.83 / 0.7605';
						  document.getElementById('method_016').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="016_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('016_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('016_rand_ker','','./rand_kernel/img_016_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_016').innerHTML = '28.59 / 0.8782';
						  document.getElementById('method_016').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="016_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('016_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('016_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('016_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('016_rand_ker','','./rand_kernel/img_016_SRF_2_HR.png',1);
						  document.getElementById('psnr_016').innerHTML = '&infin; / 1';
						  document.getElementById('method_016').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_019_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_019_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_019'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_019'>25.19 / 0.7222</b>
                        <img src="./rand_kernel/img_019_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="019_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_019_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="019_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('019_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('019_rand_ker','','./rand_kernel/img_019_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_019').innerHTML = '25.19 / 0.7222';
						  document.getElementById('method_019').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="019_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('019_rand_ker','','./rand_kernel/img_019_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_019').innerHTML = '25.96 / 0.7618';
						  document.getElementById('method_019').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="019_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('019_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('019_rand_ker','','./rand_kernel/img_019_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_019').innerHTML = '26.39 / 0.7636';
						  document.getElementById('method_019').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="019_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('019_rand_ker','','./rand_kernel/img_019_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_019').innerHTML = '27.26 / 0.8095';
						  document.getElementById('method_019').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="019_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('019_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('019_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('019_rand_ker','','./rand_kernel/img_019_SRF_2_HR.png',1);
						  document.getElementById('psnr_019').innerHTML = '&infin; / 1';
						  document.getElementById('method_019').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_020_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_020_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_020'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_020'>26.62 / 0.8333</b>
                        <img src="./rand_kernel/img_020_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="020_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_020_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="020_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('020_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('020_rand_ker','','./rand_kernel/img_020_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_020').innerHTML = '26.62 / 0.8333';
						  document.getElementById('method_020').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="020_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('020_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('020_rand_ker','','./rand_kernel/img_020_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_020').innerHTML = '27.99 / 0.8700';
						  document.getElementById('method_020').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="020_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('020_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('020_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('020_rand_ker','','./rand_kernel/img_020_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_020').innerHTML = '27.36 / 0.8535';
						  document.getElementById('method_020').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="020_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('020_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('020_rand_ker','','./rand_kernel/img_020_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_020').innerHTML = '28.45 / 0.8862';
						  document.getElementById('method_020').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="020_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('020_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('020_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('020_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('020_rand_ker','','./rand_kernel/img_020_SRF_2_HR.png',1);
						  document.getElementById('psnr_020').innerHTML = '&infin; / 1';
						  document.getElementById('method_020').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_032_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_032_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_032'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_032'>21.36 / 0.4582</b>
                        <img src="./rand_kernel/img_032_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="032_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_032_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="032_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('032_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('032_rand_ker','','./rand_kernel/img_032_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_032').innerHTML = '21.36 / 0.4582';
						  document.getElementById('method_032').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="032_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('032_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('032_rand_ker','','./rand_kernel/img_032_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_032').innerHTML = '22.00 / 0.5449';
						  document.getElementById('method_032').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="032_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('032_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('032_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('032_rand_ker','','./rand_kernel/img_032_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_032').innerHTML = '21.93 / 0.5398';
						  document.getElementById('method_032').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="032_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('032_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('032_rand_ker','','./rand_kernel/img_032_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_032').innerHTML = '22.58 / 0.6268';
						  document.getElementById('method_032').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="032_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('032_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('032_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('032_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('032_rand_ker','','./rand_kernel/img_032_SRF_2_HR.png',1);
						  document.getElementById('psnr_032').innerHTML = '&infin; / 1';
						  document.getElementById('method_032').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_034_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_034_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_034'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_034'>25.04 / 0.7874</b>
                        <img src="./rand_kernel/img_034_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="034_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_034_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="034_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('034_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('034_rand_ker','','./rand_kernel/img_034_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_034').innerHTML = '25.04 / 0.7874';
						  document.getElementById('method_034').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="034_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('034_rand_ker','','./rand_kernel/img_034_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_034').innerHTML = '26.20 / 0.8353';
						  document.getElementById('method_034').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="034_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('034_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('034_rand_ker','','./rand_kernel/img_034_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_034').innerHTML = '25.95 / 0.8281';
						  document.getElementById('method_034').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="034_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('034_rand_ker','','./rand_kernel/img_034_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_034').innerHTML = '27.23 / 0.8797';
						  document.getElementById('method_034').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="034_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('034_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('034_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('034_rand_ker','','./rand_kernel/img_034_SRF_2_HR.png',1);
						  document.getElementById('psnr_034').innerHTML = '&infin; / 1';
						  document.getElementById('method_034').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_039_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_039_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_039'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_039'>28.72 / 0.7805</b>
                        <img src="./rand_kernel/img_039_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="039_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_039_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="039_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('039_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('039_rand_ker','','./rand_kernel/img_039_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_039').innerHTML = '28.72 / 0.7805';
						  document.getElementById('method_039').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="039_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('039_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('039_rand_ker','','./rand_kernel/img_039_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_039').innerHTML = '29.59 / 0.8242';
						  document.getElementById('method_039').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="039_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('039_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('039_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('039_rand_ker','','./rand_kernel/img_039_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_039').innerHTML = '30.06 / 0.8302';
						  document.getElementById('method_039').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="039_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('039_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('039_rand_ker','','./rand_kernel/img_039_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_039').innerHTML = '31.08 / 0.8736';
						  document.getElementById('method_039').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="039_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('039_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('039_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('039_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('039_rand_ker','','./rand_kernel/img_039_SRF_2_HR.png',1);
						  document.getElementById('psnr_039').innerHTML = '&infin; / 1';
						  document.getElementById('method_039').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_047_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_047_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_047'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_047'>22.50 / 0.6036</b>
                        <img src="./rand_kernel/img_047_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="047_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_047_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="047_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('047_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('047_rand_ker','','./rand_kernel/img_047_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_047').innerHTML = '22.50 / 0.6036';
						  document.getElementById('method_047').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="047_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('047_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('047_rand_ker','','./rand_kernel/img_047_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_047').innerHTML = '23.03 / 0.6458';
						  document.getElementById('method_047').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="047_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('047_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('047_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('047_rand_ker','','./rand_kernel/img_047_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_047').innerHTML = '23.51 / 0.6765';
						  document.getElementById('method_047').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="047_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('047_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('047_rand_ker','','./rand_kernel/img_047_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_047').innerHTML = '25.48 / 0.7958';
						  document.getElementById('method_047').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="047_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('047_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('047_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('047_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('047_rand_ker','','./rand_kernel/img_047_SRF_2_HR.png',1);
						  document.getElementById('psnr_047').innerHTML = '&infin; / 1';
						  document.getElementById('method_047').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_052_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_052_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_052'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_052'>22.51 / 0.7026</b>
                        <img src="./rand_kernel/img_052_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="052_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_052_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="052_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('052_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('052_rand_ker','','./rand_kernel/img_052_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_052').innerHTML = '22.51 / 0.7026';
						  document.getElementById('method_052').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="052_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('052_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('052_rand_ker','','./rand_kernel/img_052_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_052').innerHTML = '23.22 / 0.7385';
						  document.getElementById('method_052').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="052_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('052_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('052_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('052_rand_ker','','./rand_kernel/img_052_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_052').innerHTML = '23.89 / 0.7654';
						  document.getElementById('method_052').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="052_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('052_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('052_rand_ker','','./rand_kernel/img_052_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_052').innerHTML = '26.44 / 0.8581';
						  document.getElementById('method_052').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="052_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('052_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('052_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('052_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('052_rand_ker','','./rand_kernel/img_052_SRF_2_HR.png',1);
						  document.getElementById('psnr_052').innerHTML = '&infin; / 1';
						  document.getElementById('method_052').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>


		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_071_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_071_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_071'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_071'>28.54 / 0.7626</b>
                        <img src="./rand_kernel/img_071_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="071_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_071_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="071_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('071_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('071_rand_ker','','./rand_kernel/img_071_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_071').innerHTML = '28.54 / 0.7626';
						  document.getElementById('method_071').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="071_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('071_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('071_rand_ker','','./rand_kernel/img_071_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_071').innerHTML = '28.86 / 0.7736';
						  document.getElementById('method_071').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="071_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('071_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('071_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('071_rand_ker','','./rand_kernel/img_071_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_071').innerHTML = '29.59 / 0.7976';
						  document.getElementById('method_071').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="071_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('071_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('071_rand_ker','','./rand_kernel/img_071_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_071').innerHTML = '31.05 / 0.8367';
						  document.getElementById('method_071').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="071_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('071_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('071_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('071_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('071_rand_ker','','./rand_kernel/img_071_SRF_2_HR.png',1);
						  document.getElementById('psnr_071').innerHTML = '&infin; / 1';
						  document.getElementById('method_071').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>

		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_098_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_098_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_098'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_098'>25.91 / 0.7685</b>
                        <img src="./rand_kernel/img_098_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="098_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_098_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="098_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('098_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('098_rand_ker','','./rand_kernel/img_098_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_098').innerHTML = '25.91 / 0.7685';
						  document.getElementById('method_098').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="098_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('098_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('098_rand_ker','','./rand_kernel/img_098_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_098').innerHTML = '26.42 / 0.7925';
						  document.getElementById('method_098').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="098_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('098_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('098_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('098_rand_ker','','./rand_kernel/img_098_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_098').innerHTML = '27.29 / 0.8254';
						  document.getElementById('method_098').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="098_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('098_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('098_rand_ker','','./rand_kernel/img_098_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_098').innerHTML = '29.42 / 0.8957';
						  document.getElementById('method_098').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="098_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('098_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('098_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('098_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('098_rand_ker','','./rand_kernel/img_098_SRF_2_HR.png',1);
						  document.getElementById('psnr_098').innerHTML = '&infin; / 1';
						  document.getElementById('method_098').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
		<blockquote>
        <center>
            <table style="width:75%">
                <tr>
								
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/BICUBIC_KER.png" alt="Kernel" /> <br/>The "ideal" (bicubic) downscaling kernel used to generate the training sets for SotA SR CNNs<span style="white-space: nowrap;"> (e.g. EDSR [12]).</span></td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_100_SRF_2_TRUE_KER.png" alt="Kernel" /><br/>The true (unknown) downscaling kernel used to generate the LR Input  Image from the HR image.</td>
					<td rowspan="1" width="10%" valign="top"><center><br/><br/><img src="./rand_kernel/img_100_SRF_2_EST_KER.png" alt="Kernel" /><br/>The downscaling kernel <u>estimated</u> directly from the LR test image (using [14]). This is fed to our <u>image-specific</u> CNN (ZSSR).</td>
                    <td rowspan="1" width="20%" valign="top">
						          <font size="5"><u><b id='method_100'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_100'>24.04 / 0.6759</b>
                        <img src="./rand_kernel/img_100_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="100_rand_ker" />
                    </td>

                    <td width="5%">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_kernel/img_100_SRF_2_LR.png" border="none"
                            alt="Input LR Image" />
						<br />
			

                        <button type="button" class="bic" id="100_rand_ker_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('100_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('100_rand_ker','','./rand_kernel/img_100_SRF_2_BICUBIC.png',1);
						  document.getElementById('psnr_100').innerHTML = '24.04 / 0.6759';
						  document.getElementById('method_100').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="100_rand_ker_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('100_rand_ker_bicubic').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_zssr').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('100_rand_ker','','./rand_kernel/img_100_SRF_2_EDSR.png',1);
						  document.getElementById('psnr_100').innerHTML = '24.44 / 0.7006';
						  document.getElementById('method_100').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
						<button type="button" class="kim" id="100_rand_ker_michaeli" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('100_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_edsr').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_zssr').style.fontWeight='normal';
					      document.getElementById('100_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('100_rand_ker','','./rand_kernel/img_100_SRF_2_MICHAELI.png',1);
						  document.getElementById('psnr_100').innerHTML = '25.36 / 0.7427';
						  document.getElementById('method_100').innerHTML = 'Blind-SR [14] (with estimated kernel)'">
                            Blind-SR [14] <br/> (with estimated kernel)
                        </button>
						<br />
                        <button type="button" class="osrc" id="100_rand_ker_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('100_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_michaeli').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_hr').style.fontWeight='normal';
                          MM_swapImage('100_rand_ker','','./rand_kernel/img_100_SRF_2_ZSSR.png',1);
						  document.getElementById('psnr_100').innerHTML = '27.62 / 0.8367';
						  document.getElementById('method_100').innerHTML = 'ZSSR (ours, using estimated kernel)'">
                            ZSSR (ours) <br/> (with estimated kernel)
                        </button>
						<br />
						<button type="button" class="freeman" id="100_rand_ker_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('100_rand_ker_bicubic').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_edsr').style.fontWeight='normal';
						  document.getElementById('100_rand_ker_michaeli').style.fontWeight='normal';
                          document.getElementById('100_rand_ker_zssr').style.fontWeight='normal';
                          MM_swapImage('100_rand_ker','','./rand_kernel/img_100_SRF_2_HR.png',1);
						  document.getElementById('psnr_100').innerHTML = '&infin; / 1';
						  document.getElementById('method_100').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
	
	    <hr />
		</center>
	<a id="rand_deg"><span style="font-weight: bold; font-size: 1.5em; color:red; background-color: #cccccc;">3. SR of poor-quality LR images</span><span style="font-size: 1.5em; color:red;"> (The random degradation experiment)</span> </a><br/> <font size="5">
	        <ul>
<li>	LR images were <b>randomly contaminated</b> using one of 3 types of image degradations (e.g., noise, compression artifacts, etc. -- see Sec. 4.2 in the paper for more details). The type of degradation is unknown to the SR algorithm. </li>
<li>         <b>SR methods tend to magnify the noise together with the image details.</b> They increase all high frequencies in the image (even subtle noise is magnified).</li>
<li>           Image-specific CNN (ZSSR) is relatively robust to unknown degradation. It magnifies details, while eliminating the noise. We attribute this phenomenon to the fact that <b>image-specific details tend to recur across image scales, whereas noise artifacts do not</b> (see Sec. 3.2 in the paper for more details). </li>
</font>
</ul>
<span style="font-weight: bold; font-size: 1.7em;"> Below we show a few sample images. Extensive empirical evaluation on the full dataset of 100 images can be found in the paper.</span>
 <hr />
		
	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"><u><b id='method_067_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_067_n'>36.44 / 0.9555</b>
							<br/>
                        <img src="./rand_degrade/img_067_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="067_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_067_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="067_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('067_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('067_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('067_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_067_n').innerHTML = '36.44 / 0.9555';
                          MM_swapImage('067_rand_deg','','./rand_degrade/img_067_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_067_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="067_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('067_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('067_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('067_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_067_n').innerHTML = '35.88 / 0.9467';
                          MM_swapImage('067_rand_deg','','./rand_degrade/img_067_SRF_2_EDSR.png',1);
						  document.getElementById('method_067_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="067_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('067_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('067_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('067_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_067_n').innerHTML = '37.80 / 0.9696';
                          MM_swapImage('067_rand_deg','','./rand_degrade/img_067_SRF_2_ZSSR.png',1);
						  document.getElementById('method_067_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="067_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('067_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('067_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('067_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_067_n').innerHTML = '&infin; / 1';
                          MM_swapImage('067_rand_deg','','./rand_degrade/img_067_SRF_2_HR.png',1);
						  document.getElementById('method_067_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>

	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"><u><b id='method_079_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_079_n'>29.73 / 0.9044</b>
							<br/>
                        <img src="./rand_degrade/img_079_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="079_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_079_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="079_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('079_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('079_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('079_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_079_n').innerHTML = '29.73 / 0.9044';
                          MM_swapImage('079_rand_deg','','./rand_degrade/img_079_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_079_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="079_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('079_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('079_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('079_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_079_n').innerHTML = '29.82 / 0.8912';
                          MM_swapImage('079_rand_deg','','./rand_degrade/img_079_SRF_2_EDSR.png',1);
						  document.getElementById('method_079_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="079_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('079_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('079_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('079_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_079_n').innerHTML = '31.46 / 0.9355';
                          MM_swapImage('079_rand_deg','','./rand_degrade/img_079_SRF_2_ZSSR.png',1);
						  document.getElementById('method_079_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="079_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('079_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('079_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('079_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_079_n').innerHTML = '&infin; / 1';
                          MM_swapImage('079_rand_deg','','./rand_degrade/img_079_SRF_2_HR.png',1);
						  document.getElementById('method_079_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>

	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"><u><b id='method_034_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_034_n'>25.38 / 0.6948</b>
							<br/>
                        <img src="./rand_degrade/img_034_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="034_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_034_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="034_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('034_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('034_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('034_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_034_n').innerHTML = '25.38 / 0.6948';
                          MM_swapImage('034_rand_deg','','./rand_degrade/img_034_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_034_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="034_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('034_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('034_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_034_n').innerHTML = '24.91 / 0.5953';
                          MM_swapImage('034_rand_deg','','./rand_degrade/img_034_SRF_2_EDSR.png',1);
						  document.getElementById('method_034_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="034_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('034_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('034_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_034_n').innerHTML = '26.25 / 0.8253';
                          MM_swapImage('034_rand_deg','','./rand_degrade/img_034_SRF_2_ZSSR.png',1);
						  document.getElementById('method_034_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="034_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('034_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('034_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('034_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_034_n').innerHTML = '&infin; / 1';
                          MM_swapImage('034_rand_deg','','./rand_degrade/img_034_SRF_2_HR.png',1);
						  document.getElementById('method_034_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"><u><b id='method_019_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_019_n'>25.79 / 0.7097</b>
							<br/>
                        <img src="./rand_degrade/img_019_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="019_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_019_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="019_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('019_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('019_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('019_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_019_n').innerHTML = '25.79 / 0.7097';
                          MM_swapImage('019_rand_deg','','./rand_degrade/img_019_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_019_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="019_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('019_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('019_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_019_n').innerHTML = '25.68 / 0.6954';
                          MM_swapImage('019_rand_deg','','./rand_degrade/img_019_SRF_2_EDSR.png',1);
						  document.getElementById('method_019_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="019_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('019_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('019_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_019_n').innerHTML = '26.41 / 0.7268';
                          MM_swapImage('019_rand_deg','','./rand_degrade/img_019_SRF_2_ZSSR.png',1);
						  document.getElementById('method_019_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="019_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('019_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('019_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('019_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_019_n').innerHTML = '&infin; / 1';
                          MM_swapImage('019_rand_deg','','./rand_degrade/img_019_SRF_2_HR.png',1);
						  document.getElementById('method_019_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"><u><b id='method_049_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_049_n'>28.27 / 0.8974</b>
							<br/>
                        <img src="./rand_degrade/img_049_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="049_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_049_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="049_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('049_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('049_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('049_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_049_n').innerHTML = '28.27 / 0.8974';
                          MM_swapImage('049_rand_deg','','./rand_degrade/img_049_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_049_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="049_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('049_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('049_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('049_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_049_n').innerHTML = '30.10 / 0.8882';
                          MM_swapImage('049_rand_deg','','./rand_degrade/img_049_SRF_2_EDSR.png',1);
						  document.getElementById('method_049_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="049_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('049_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('049_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('049_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_049_n').innerHTML = '30.86 / 0.9321';
                          MM_swapImage('049_rand_deg','','./rand_degrade/img_049_SRF_2_ZSSR.png',1);
						  document.getElementById('method_049_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="049_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('049_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('049_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('049_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_049_n').innerHTML = '&infin; / 1';
                          MM_swapImage('049_rand_deg','','./rand_degrade/img_049_SRF_2_HR.png',1);
						  document.getElementById('method_049_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>

	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"><u><b id='method_062_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_062_n'>28.94 / 0.7711</b>
							<br/>
                        <img src="./rand_degrade/img_062_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="062_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_062_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="062_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('062_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('062_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('062_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_062_n').innerHTML = '28.94 / 0.7711';
                          MM_swapImage('062_rand_deg','','./rand_degrade/img_062_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_062_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="062_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('062_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('062_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('062_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_062_n').innerHTML = '28.63 / 0.7603';
                          MM_swapImage('062_rand_deg','','./rand_degrade/img_062_SRF_2_EDSR.png',1);
						  document.getElementById('method_062_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="062_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('062_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('062_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('062_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_062_n').innerHTML = '29.26 / 0.7784';
                          MM_swapImage('062_rand_deg','','./rand_degrade/img_062_SRF_2_ZSSR.png',1);
						  document.getElementById('method_062_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="062_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('062_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('062_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('062_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_062_n').innerHTML = '&infin; / 1';
                          MM_swapImage('062_rand_deg','','./rand_degrade/img_062_SRF_2_HR.png',1);
						  document.getElementById('method_062_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
	<blockquote>
        <center>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							          <font size="5"> <u><b id='method_060_n'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_060_n'>29.44 / 0.6763</b>
							<br/>
                        <img src="./rand_degrade/img_060_SRF_2_BICUBIC.png" alt="High Resolution Image"
                            id="060_rand_deg" />
                    </td>

                    <td  valign="top">
                         <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./rand_degrade/img_060_SRF_2_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="060_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('060_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('060_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('060_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_060_n').innerHTML = '29.44 / 0.6763';
                          MM_swapImage('060_rand_deg','','./rand_degrade/img_060_SRF_2_BICUBIC.png',1);
						  document.getElementById('method_060_n').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="060_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('060_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('060_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('060_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_060_n').innerHTML = '27.32 / 0.5430';
                          MM_swapImage('060_rand_deg','','./rand_degrade/img_060_SRF_2_EDSR.png',1);
						  document.getElementById('method_060_n').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="060_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('060_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('060_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('060_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_060_n').innerHTML = '30.78 / 0.7645';
                          MM_swapImage('060_rand_deg','','./rand_degrade/img_060_SRF_2_ZSSR.png',1);
						  document.getElementById('method_060_n').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="060_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('060_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('060_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('060_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_060_n').innerHTML = '&infin; / 1';
                          MM_swapImage('060_rand_deg','','./rand_degrade/img_060_SRF_2_HR.png',1);
						  document.getElementById('method_060_n').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>




	<hr /></center>
	<a id="additional"><span style="font-weight: bold; font-size: 1.5em; color:red; background-color: #cccccc;">4. Remaining images from the paper figures. (All other images from the paper figures were included above).</span> </a></h2>
        <hr />
		
<blockquote>
        <center>
		<span style="font-weight: bold; font-size: 1.5em; "><u>Ideally (bicubic) downscaled image with strong internal repetitive structures - SR x3 </u></span><br/>
            <table style="width:40%">
                <tr>
                    <td rowspan="1" width="70%" valign="top">
							 <font size="5"><u><b id='method_eyechart'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_eyechart'>17.20 / 0.7872</b>
							<br/>
                        <img src="./additional/eyechart_BICUBIC.png" alt="High Resolution Image"
                            id="eyechart_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./additional/eyechart_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="eyechart_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('eyechart_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_vdsr').style.fontWeight='normal';
                          document.getElementById('eyechart_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_eyechart').innerHTML = '17.20 / 0.7872';
                          MM_swapImage('eyechart_rand_deg','','./additional/eyechart_BICUBIC.png',1);
						  document.getElementById('method_eyechart').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
						<br />
                        <button type="button" class="kim" id="eyechart_rand_deg_vdsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('eyechart_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('eyechart_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_eyechart').innerHTML = '20.11 / 0.9136';
                          MM_swapImage('eyechart_rand_deg','','./additional/eyechart_VDSR.png',1);
						  document.getElementById('method_eyechart').innerHTML = 'VDSR [8]'">
                            VDSR [8]
                        </button>
                        <br />
                        <button type="button" class="fattal" id="eyechart_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('eyechart_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('eyechart_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_vdsr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_eyechart').innerHTML = '25.29 / 0.9627';
                          MM_swapImage('eyechart_rand_deg','','./additional/eyechart_EDSR.png',1);
						  document.getElementById('method_eyechart').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="eyechart_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('eyechart_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('eyechart_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_vdsr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_eyechart').innerHTML = '25.68 / 0.9546';
                          MM_swapImage('eyechart_rand_deg','','./additional/eyechart_ZSSR.png',1);
						  document.getElementById('method_eyechart').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="eyechart_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('eyechart_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('eyechart_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('eyechart_rand_deg_vdsr').style.fontWeight='normal';
                          document.getElementById('eyechart_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_eyechart').innerHTML = '&infin; / 1';
                          MM_swapImage('eyechart_rand_deg','','./additional/eyechart_HR.png',1);
						  document.getElementById('method_eyechart').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
<blockquote>
        <center>
		<span style="font-weight: bold; font-size: 1.5em; "><u>SR under Aliasing (LR was sampled by a Delta-function) - SR x2 </u></span><br/>
            <table style="width:20%">
                <tr>
                    <td rowspan="1" width="20%" valign="top">
							 <font size="5"><u><b id='method_alias'>Bi-Cubic Interpolation</b><br/></font> </u>(PSNR / SSIM) = <b id='psnr_alias'>29.48 / 0.8204</b>
							<br/>
                        <img src="./additional/alias_BICUBIC.png" alt="High Resolution Image"
                            id="alias_rand_deg" />
                    </td>

                    <td  valign="top">
                        <font size="5">Input LR Image</font>
                        <br /><br />
                        <img src="./additional/alias_LR.png" border="none"
                            alt="Input image" />

                        <button type="button" class="bic" id="alias_rand_deg_bicubic" onmousedown="this.style.fontWeight='bold';
                          document.getElementById('alias_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('alias_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('alias_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_alias').innerHTML = '29.48 / 0.8204';
                          MM_swapImage('alias_rand_deg','','./additional/alias_BICUBIC.png',1);
						  document.getElementById('method_alias').innerHTML = 'Bi-Cubic Interpolation'">
                            Bi-Cubic Interpolation
                        </button>
                        <br />
                        <button type="button" class="fattal" id="alias_rand_deg_edsr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('alias_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('alias_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('alias_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_alias').innerHTML = '29.69 / 0.7572';
                          MM_swapImage('alias_rand_deg','','./additional/alias_EDSR.png',1);
						  document.getElementById('method_alias').innerHTML = 'EDSR+ [12]'">
                            EDSR+ [12]
                        </button>
                        <br />
                        <button type="button" class="osrc" id="alias_rand_deg_zssr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('alias_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('alias_rand_deg_edsr').style.fontWeight='normal';
						  document.getElementById('alias_rand_deg_hr').style.fontWeight='normal';
						  document.getElementById('psnr_alias').innerHTML = '30.58 / 0.8796';
                          MM_swapImage('alias_rand_deg','','./additional/alias_ZSSR.png',1);
						  document.getElementById('method_alias').innerHTML = 'ZSSR (ours)'">
                            ZSSR (ours)
                        </button>
						<br />
						<button type="button" class="freeman" id="alias_rand_deg_hr" onmousedown="this.style.fontWeight='bold';
						  document.getElementById('alias_rand_deg_bicubic').style.fontWeight='normal';
                          document.getElementById('alias_rand_deg_edsr').style.fontWeight='normal';
                          document.getElementById('alias_rand_deg_zssr').style.fontWeight='normal';
						  document.getElementById('psnr_alias').innerHTML = '&infin; / 1';
                          MM_swapImage('alias_rand_deg','','./additional/alias_HR.png',1);
						  document.getElementById('method_alias').innerHTML = 'Ground truth'">
                            Ground truth
                        </button>
                    </td>
                </tr>
            </table>
        </center>
    </blockquote>
	</body>
</html>
