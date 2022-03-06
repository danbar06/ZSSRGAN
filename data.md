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
        <tr class="shadow f1_card">
            <td rowspan="1" valign="top">
                <img src="Lincoln_ZSSR.png" id="Lincoln switch"/>
            </td>
            <td rowspan="1" valign="top">
                <img src="Lincoln.png"/>
            </td>
            <td>
                <button onclick="change_img('Lincoln', 'ZSSR')" 
      style="font-size: 12px;background-color:lightgreen">ZSSR</button>
                <br>
                <button onclick="change_img('Lincoln', 'ZSSRGAN')"
      style="font-size: 12px;background-color:lightblue">ZSSRGAN (Ours)</button>
                <br>
                <button onclick="change_img('Lincoln', 'KERGAN')"
      style="font-size: 12px;background-color:tomato">KernelGAN</button>
            </td>
        </tr>
    </tbody>
</table>

</body>
<script>
function change_img(name, method) {
  document.getElementById(name + " switch").src = "../ZSSRGAN/" + name + "_" + method + ".png";
}
</script>
</html>
