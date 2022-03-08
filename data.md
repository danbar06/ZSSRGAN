<html style="height:100%;">
<head>
<style>
body { position:absolute; top:0; bottom:0; right:0; left:0; }
table, th, td {
  border: 0px solid black;
}
</style>
</head>
<body>

<span style="font-weight: bold; font-size: 1.5em; "><u>Historic image: Abraham Lincoln photograph - SR x2 </u></span>
<table>
    <tbody>
        <tr>
            <td>
              <font size="5"><u><b id="Lincoln text">ZSSRGAN</b><br></u></font>
                <img src="../ZSSRGAN/data/Lincoln_ZSSRGAN.png" id="Lincoln img">
            </td>
            <td style="vertical-align:bottom">
                <button onclick="change_img('Lincoln', 'ZSSR')" style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('Lincoln', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('Lincoln', 'KERGAN')" style="font-size: 12px;background-color:tomato">KernelGAN</button>
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
                <button onclick="change_img('cars', 'ZSSR')" style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('cars', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('cars', 'KERGAN')" style="font-size: 12px;background-color:tomato">KernelGAN</button>
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
                <button onclick="change_img('charlie', 'ZSSR')" style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('charlie', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('charlie', 'KERGAN')" style="font-size: 12px;background-color:tomato">KernelGAN</button>
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
                <button onclick="change_img('flowers', 'ZSSR')" style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('flowers', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('flowers', 'KERGAN')" style="font-size: 12px;background-color:tomato">KernelGAN</button>
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
                <button onclick="change_img('salamandra', 'ZSSR')" style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('salamandra', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('salamandra', 'KERGAN')" style="font-size: 12px;background-color:tomato">KernelGAN</button>
                <br>
                <img src="../ZSSRGAN/data/salamandra.png">
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
  return "ZSSR";
}
function change_img(name, method) {
  document.getElementById(name + " img").src = "../ZSSRGAN/data/" + name + "_" + method + ".png";
  document.getElementById(name + " text").innerHTML = get_name(method);
}
</script>
</html>
