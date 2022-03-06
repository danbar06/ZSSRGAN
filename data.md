## Historic image: Check-point Charlie (end of World-War II) - SR x2
# Real image
<div class="f1_container">
    <div class="shadow f1_card">
        <div class="front face" id="Lincoln">
            <img src="Lincoln.png"/>
        </div>
        <div class="front face">
            <img src="Lincoln_ZSSR.png" id="Lincoln-switch"/>
            <button onclick="zssrgan(Lincoln-switch)">Click me</button>
        </div>
    </div>
</div>

<script>
function zssrgan(name) {
  print("name: " + name)
  document.getElementById(name).src = name + "_ZSSRGAN.png";
}
</script>
