## Historic image: Check-point Charlie (end of World-War II) - SR x2
# Real image
<div class="f1_container">
    <div class="shadow f1_card">
        <div class="front face" id="Lincoln">
            <img src="Lincoln.png"/>
        </div>
        <div class="front face">
            <img src="Lincoln_ZSSR.png" id="Lincoln switch"/>
            <br>
            <button onclick="change_img('Lincoln', 'ZSSRGAN')">ZSSRGAN (Ours)</button>
            <button onclick="change_img('Lincoln', 'ZSSR')">ZSSR</button>
            <button onclick="change_img('Lincoln', 'KERGAN')">KernelGAN</button>
        </div>
    </div>
</div>

<script>
function change_img(name, method) {
  document.getElementById(name + " switch").src = "../ZSSRGAN/" + name + "_" + method + ".png";
}
</script>
