## Historic image: Abraham Lincoln photograph - SR x2
<div class="f1_container">
    <tr class="shadow f1_card">
        <td rowspan="1" width="20%" valign="top">
            <img src="Lincoln.png"/>
        </td>
        <td valign="top">
            <img src="Lincoln_ZSSR.png" id="Lincoln switch"/>
            <br>
            <button onclick="change_img('Lincoln', 'ZSSR')" 
  style="background-color:lightgreen">ZSSR</button>
            <button onclick="change_img('Lincoln', 'ZSSRGAN')">ZSSRGAN (Ours)</button>
            <button onclick="change_img('Lincoln', 'KERGAN')">KernelGAN</button>
        </td>
    </tr>
</div>
            
<script>
function change_img(name, method) {
  document.getElementById(name + " switch").src = "../ZSSRGAN/" + name + "_" + method + ".png";
}
</script>
