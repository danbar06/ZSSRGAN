## Historic image: Abraham Lincoln photograph - SR x2

<html>
<head>
<style>
table, th, td {
  border: 0px solid black;
}
</style>
</head>
<body>

<table>
    <tbody>
        <tr>
            <td>
              <font size="5"><u><b id="Lincoln text">ZSSRGAN</b><br></u></font>
                <img src="../ZSSRGAN/Lincoln_ZSSRGAN.png" id="Lincoln img">
            </td>
            <td style="vertical-align:bottom">
                <button onclick="change_img('Lincoln', 'ZSSR')" style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('Lincoln', 'ZSSRGAN')" style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('Lincoln', 'KERGAN')" style="font-size: 12px;background-color:tomato">KernelGAN</button>
                <br>
                <img src="Lincoln.png">
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
  document.getElementById(name + " img").src = "../ZSSRGAN/" + name + "_" + method + ".png";
  document.getElementById(name + " text").innerHTML = get_name(method);
}
</script>
</html>
