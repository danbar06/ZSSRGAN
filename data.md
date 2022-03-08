<html style="width: 100%;height:100%;">
<head>
<style>
body { position:absolute; top:0; bottom:0; right:0; left:0; }
table, th, td {
  border: 0px solid black;
}
img {width:auto; height:auto;}
</style>
</head>
<body style="width: 200%;">

  <div>
    <span style="font-weight: bold; font-size: 1.5em; "><u>Historic image: Abraham Lincoln photograph - SR x2 </u></span>
    <table>
        <tbody>
            <tr>
                <td>
                  <font size="5"><u><b id="Lincoln text">ZSSRGAN</b><br></u></font>
                    <img src="../ZSSRGAN/data/Lincoln_ZSSRGAN.png" id="Lincoln img">
                </td>
                <td style="vertical-align:bottom">
                    <button onclick="change_img('Lincoln', 'ZSSR')" style="font-size: 12px;background-color:lightgreen" class="button zssr">ZSSR</button>
                    <br>
                    <button onclick="change_img('Lincoln', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue" class="button zssrgan">ZSSRGAN (Ours)</button>
                    <br>
                    <button onclick="change_img('Lincoln', 'KERGAN')" style="font-size: 12px;background-color:tomato" class="button kergan">KernelGAN</button>
                    <br>
                    <img src="../ZSSRGAN/data/Lincoln.png">
                </td>
            </tr>
        </tbody>
    </table>
    <br>
    <span style="font-weight: bold; font-size: 1.5em; "><u>Colored image: A garage with cars - SR x2 </u></span>
    <table>
        <tbody>
            <tr>
                <td>
                  <font size="5"><u><b id="cars text">ZSSRGAN</b><br></u></font>
                    <img src="../ZSSRGAN/data/cars_ZSSRGAN.png" id="cars img">
                </td>
                <td style="vertical-align:bottom">
                    <button onclick="change_img('cars', 'ZSSR')" style="font-size: 12px;background-color:lightgreen" class="button zssr">ZSSR</button>
                    <br>
                    <button onclick="change_img('cars', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue" class="button zssrgan">ZSSRGAN (Ours)</button>
                    <br>
                    <button onclick="change_img('cars', 'KERGAN')" style="font-size: 12px;background-color:tomato" class="button kergan">KernelGAN</button>
                    <br>
                    <img src="../ZSSRGAN/data/cars.png">
                </td>
            </tr>
        </tbody>
    </table>
    <br>
    <span style="font-weight: bold; font-size: 1.5em; "><u>Historic image: Check-point Charlie (end of World-War II) - SR x2 </u></span>
    <table>
        <tbody>
            <tr>
                <td>
                  <font size="5"><u><b id="charlie text">ZSSRGAN</b><br></u></font>
                    <img src="../ZSSRGAN/data/charlie_ZSSRGAN.png" id="charlie img">
                </td>
                <td style="vertical-align:bottom">
                    <button onclick="change_img('charlie', 'ZSSR')" style="font-size: 12px;background-color:lightgreen" class="button zssr">ZSSR</button>
                    <br>
                    <button onclick="change_img('charlie', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue" class="button zssrgan">ZSSRGAN (Ours)</button>
                    <br>
                    <button onclick="change_img('charlie', 'KERGAN')" style="font-size: 12px;background-color:tomato" class="button kergan">KernelGAN</button>
                    <br>
                    <img src="../ZSSRGAN/data/charlie.png">
                </td>
            </tr>
        </tbody>
    </table>
    <br>
    <span style="font-weight: bold; font-size: 1.5em; "><u>Colored image: Flowers - SR x2 </u></span>
    <table>
        <tbody>
            <tr>
                <td>
                  <font size="5"><u><b id="flowers text">ZSSRGAN</b><br></u></font>
                    <img src="../ZSSRGAN/data/flowers_ZSSRGAN.png" id="flowers img">
                </td>
                <td style="vertical-align:bottom">
                    <button onclick="change_img('flowers', 'ZSSR')" style="font-size: 12px;background-color:lightgreen" class="button zssr">ZSSR</button>
                    <br>
                    <button onclick="change_img('flowers', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue" class="button zssrgan">ZSSRGAN (Ours)</button>
                    <br>
                    <button onclick="change_img('flowers', 'KERGAN')" style="font-size: 12px;background-color:tomato" class="button kergan">KernelGAN</button>
                    <br>
                    <img src="../ZSSRGAN/data/flowers.png">
                </td>
            </tr>
        </tbody>
    </table>
    <br>
    <span style="font-weight: bold; font-size: 1.5em; "><u>Colored image: Gaudi's Salamandra - SR x2 </u></span>
    <table>
        <tbody>
            <tr>
                <td>
                  <font size="5"><u><b id="salamandra text">ZSSRGAN</b><br></u></font>
                    <img src="../ZSSRGAN/data/salamandra_ZSSRGAN.png" id="salamandra img">
                </td>
                <td style="vertical-align:bottom">
                    <button onclick="change_img('salamandra', 'ZSSR')" style="font-size: 12px;background-color:lightgreen" class="button zssr">ZSSR</button>
                    <br>
                    <button onclick="change_img('salamandra', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue" class="button zssrgan">ZSSRGAN (Ours)</button>
                    <br>
                    <button onclick="change_img('salamandra', 'KERGAN')" style="font-size: 12px;background-color:tomato" class="button kergan">KernelGAN</button>
                    <br>
                    <img src="../ZSSRGAN/data/salamandra.png">
                </td>
            </tr>
        </tbody>
    </table>
  </div>
</body>
<script>
function get_name(name){
  if (name == "ZSSRGAN"){
    return "ZSSRGAN (Ours)";
  }
  if (name == "KERGAN"){
    return "KernelGAN";
  }
  return name;
}
function change_img(name, method) {
  document.getElementById(name + " img").src = "../ZSSRGAN/data/" + name + "_" + method + ".png";
  document.getElementById(name + " text").innerHTML = get_name(method);
}
window.scrollTo({ top: 0, left: 1150, behavior: 'smooth'});
</script>
</html>

Our method learn the down scaled kernel of an image and utilize it in order to preduce a SR image, the same task that KernelGAN are solving.
ZSSR on the other hand together the Bicubic kernel (its most basic configuration), is better at solving an artificially down scaled images since it assume the kernel is the same kernel used for down scaling (Bicubic), while our method and KernelGAN are learing this kernel.
In the next example, we took such an image that down scaled artificially using the Bicubic algorithm.
<html style="width: 100%;height:100%;">
<head>
<style>
body { position:absolute; top:0; bottom:0; right:0; left:0; }
table, th, td {
  border: 0px solid black;
}
img {width:auto; height:auto;}
</style>
</head>
<body style="width: 200%;">
    <span style="font-weight: bold; font-size: 1.5em; "><u>Artificially down scaled image: Baby - SR x2 </u></span>
    <table>
        <tbody>
            <tr>
                <td>
                  <font size="5"><u><b id="baby text">ZSSRGAN</b><br></u></font>
                  <font size="5"><u><b id="psnr text">(PSNR/SSIM) 28.566/0.951</b><br></u></font>
                    <img src="../ZSSRGAN/data/baby_ZSSRGAN.png" id="baby img">
                </td>
                <td style="vertical-align:bottom">
                    <button onclick="change_img('baby', 'ZSSR')" style="font-size: 12px;background-color:lightgreen" class="button zssr">ZSSR</button>
                    <br>
                    <button onclick="change_img('baby', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue" class="button zssrgan">ZSSRGAN (Ours)</button>
                    <br>
                    <button onclick="change_img('baby', 'KERGAN')" style="font-size: 12px;background-color:tomato" class="button kergan">KernelGAN</button>
                    <br>
                    <button onclick="change_img('baby', 'GT')" style="font-size: 12px;background-color:Lime" class="button gt">Ground Truth</button>
                </td>
            </tr>
        </tbody>
    </table>
</body>
<script>
function get_name(name){
  if (name == "ZSSRGAN"){
    return "ZSSRGAN (Ours)";
  }
  if (name == "KERGAN"){
    return "KernelGAN";
  }
  if (name == "GT"){
    return "Ground Truth";
  }
  return name;
}
function get_psnr(name){
  if (name == "ZSSRGAN"){
    return "31.051/0.968";
  }
  if (name == "KERGAN"){
    return "25.25/0.922";
  }
  if (name == "ZSSR"){
    return "38.015/0.997";
  }
  return "∞/1";
}
function change_img(name, method) {
  document.getElementById(name + " img").src = "../ZSSRGAN/data/" + name + "_" + method + ".png";
  document.getElementById(name + " text").innerHTML = get_name(method);
  if (name == 'baby'){
    document.getElementById('psnr text').innerHTML = "(PSNR/SSIM) " + get_psnr(method);
  }
}
</script>
</html>
