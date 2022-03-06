## Historic image: Check-point Charlie (end of World-War II) - SR x2
# Real image
<div class="f1_container">
    <div class="shadow f1_card">
        <div class="front face" id="Lincoln">
            <img src="data/Lincoln.png"/>
        </div>
        <div class="front face">
            <img src="data/Lincoln_zssr.png"/>
            <button name="Lincoln" onclick="zssr(this)">Click me</button>
        </div>
    </div>
</div>

<script>
function zssr(this) {
  document.getElementById(this.name).src = this.name + "_ZSSR.png";
}
</script>
