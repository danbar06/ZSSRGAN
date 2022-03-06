## Historic image: Abraham Lincoln photograph - SR x2
<div class="f1_container">
    <table>
        <tr class="shadow f1_card">
            <td rowspan="1" valign="top">
                <img src="Lincoln.png"/>
                <br>
                <button onclick="change_img('Lincoln', 'ZSSR')" 
      style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('Lincoln', 'ZSSRGAN')"
      style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('Lincoln', 'KERGAN')"
      style="font-size: 12px;background-color:tomato">KernelGAN</button>
            </td>
            <td valign="top">
                <img src="Lincoln_ZSSR.png" id="Lincoln switch"/>
            </td>
        </tr>
    <\table>
</div>
            
<script>
function change_img(name, method) {
  document.getElementById(name + " switch").src = "../ZSSRGAN/" + name + "_" + method + ".png";
}
</script>
