# Historic image: Check-point Charlie (end of World-War II) - SR x2
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
