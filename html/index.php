<div id="titles">
<h1><u>Colors</u></h1>

<h1><u>Brightness</u></h1>

<h1><u>Time</u></h1>
</div>


<?php

echo '<link rel="stylesheet" type="text/css" href="css/main.css"/>';

	if(isset($_POST['red'])){
	exec("php red.php");
	echo "<div style='font-size:1.25em;'> Red color selected </div>";
}elseif(isset($_POST['green'])){
	exec("php green.php");
	echo "<div style='font-size:1.25em;'> Green color selected </div>";
}elseif(isset($_POST['blue'])){
	exec("php blue.php");
	echo "<div style='font-size:1.25em;'> Blue color selected </div>";
}elseif(isset($_POST['pink'])){
	exec("php pink.php");
	echo "<div style='font-size:1.25em;'> Pink color selected </div>";
}elseif(isset($_POST['orange'])){
	exec("php orange.php");
	echo "<div style='font-size:1.25em;'> Orange color selected </div>";
}elseif(isset($_POST['white'])){
	exec("php white.php");
	echo "<div style='font-size:1.25em;'> White color selected </div>";
}elseif(isset($_POST['rainbow'])){
	exec("php rainbow.php");
	echo "<div style='font-size:1.25em;'> Rainbow mode selected </div>";
}elseif(isset($_POST['rainbow2'])){
	exec("php rainbow2.php");
	echo "<div style='font-size:1.25em;'> Rainbow2 mode selected </div>";
}elseif(isset($_POST['wild'])){
	exec("php wild.php");
	echo "<div style='font-size:1.25em;'> Wild mode selected </div>";
}elseif(isset($_POST['colorStripes'])){
	exec("php colorStripes.php");
	echo "<div style='font-size:1.25em;'> Color Stripes mode selected </div>";
}elseif(isset($_POST['christmas'])){
	exec("php christmas.php");
	echo "<div style='font-size:1.25em;'> Christmas mode selected </div>";
}elseif(isset($_POST['weather'])){
	exec("php weather.php");
	echo "<div style='font-size:1.25em;'> Weather Mode Selected </div>";
}elseif(isset($_POST['none'])){
	exec("php none.php");
	echo "<div style='font-size:1.25em;'> No Color Selected </div>";
}elseif(isset($_POST['low'])){
	exec("php low.php");
	echo "<div style='font-size:1.25em;'> Low Brightness Selected </div>";
}elseif(isset($_POST['medium'])){
	exec("php medium.php");
	echo "<div style='font-size:1.25em;'> Medium Brightness Selected </div>";
}elseif(isset($_POST['high'])){
	exec("php high.php");
	echo "<div style='font-size:1.25em;'> High Brightness Selected </div>";
}elseif(isset($_POST['nineWeather'])){
	exec("php nineWeather.php");
	echo "<div style='font-size:1.25em;'> Showing weather at 9:00 A.M </div>";
}elseif(isset($_POST['threeWeather'])){
	exec("php threeWeather.php");
	echo "<div style='font-size:1.25em;'> Showing weather at 3:00 P.M </div>";
}elseif(isset($_POST['weatherNine'])){
	exec("php weatherNine.php");
	echo "<div style='font-size:1.25em;'> Showing weather at 9:00 P.M </div>";
}elseif(isset($_POST['nextWeather'])){
	exec("php nextWeather.php");
	echo "<div style='font-size:1.25em;'> Showing weather at 9:00 A.M tomorrow morning </div>";
}elseif(isset($_POST['settime'])){
	$dbb = new SQLite3('/var/www/html/led_db');
	$statement=$dbb->prepare('UPDATE mode SET alarmHour=:hour, alarmMinute=:minute, alarmMode=:mode');
	$statement->bindParam(':hour', $_POST['hour']);
	$statement->bindParam(':minute', $_POST['minute']);
	$statement->bindParam(':mode', $_POST['ampm']);
	$statement->execute();
	echo "<div style='font-size:1.25em;'> Weather mode will turn on at <b>".$_POST['hour'].":".$_POST['minute']." ".$_POST['ampm']."</b></div>";
}elseif(isset($_POST['alarmOff'])){
	$dbb = new SQLite3('/var/www/html/led_db');
	$statement=$dbb->prepare('UPDATE mode SET alarmHour=0, alarmMinute=00, alarmMode="am"');
	$statement->execute();
	echo "<div style='font-size:1.25em;'>Alarm Off</div>";
}elseif(isset($_POST['shutdown'])){
	exec("php shutdown.php");
	echo "<div style='font-size:1.25em;'> Raspberry Pi is shutting down. Wait 10 seconds to unplug it. To power back on, plug into wall again</div>";
}

?>

<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/main.css">
<meta name="viewport" content="width=device-width, initial-scale=1" /> 
</head>
<body>
<div id="colors">
<form action="" method="post">
	<input type="submit" name="red" value="Red" id="red" style="background-color: rgb(255, 100, 100);">
</form>
<form action="" method="post">
	<input type="submit" name = "green" value="Green" style="background-color: rgb(0, 200, 0);">
</form>
<form action="" method="post">
	<input type="submit" name="blue" value="Blue" style="background-color: rgb(100, 100, 255);">
</form>
<form action="" method="post">
	<input type="submit" name="pink" value="Pink" style="background-color: rgb(255, 170, 220);">
</form>
<form action="" method="post">
	<input type="submit" name="orange" value="Orange" style="background-color: rgb(255, 150, 0);">
</form>
<form action="" method="post">
	<input type="submit" name="white" value="White" style="background-color: rgb(255, 255, 255);">
</form>
<form action="" method="post">
	<input type="submit" name="rainbow" value="Rainbow" id="rainbow1" style="background-image: url('images/rainbow1.jpg'); font-size:100%">
</form>
<form action="" method="post">
	<input type="submit" name="rainbow2" value="Rainbow2" id="rainbow2" style="background-image: url('images/rainbow2.png'); font-size:100%;">
</form>
<form action="" method="post">
	<input type="submit" name="wild" value="Wild">
</form>
<form action="" method="post">
	<input type="submit" name="colorStripes" style="font-size:100%;" value="Color Stripes">
</form>
<form action="" method="post">
	<input type="submit" name="christmas" style="font-size:100%;" value="Christmas">
</form>
<form action="" method="post">
	<input type="submit" name="weather" value="Weather" style="font-size:100%;">
</form>  
<form action="" method="post">
	<input type="submit" name="none" value="OFF">
</form>
<form action="" method="post">
	<input type="submit" name="shutdown" value="SHUTDOWN" id="shutdown" style="font-size:100%;">
</form>
</div>

<div id="brightness">
<form action="" method="post">
	<input type="submit" name="low" value="Low">
</form>
<form action="" method="post">
	<input type="submit" name="medium" value="Medium">
</form>
<form action="" method="post">
	<input type="submit" name="high" value="High">
</form>
<form action="" method="post">
	<input type="submit" name="nineWeather" value="9:00 A.M Weather" style="margin-top: 66px; font-size:100%;">
</form>
<form action="" method="post">
	<input type="submit" name="threeWeather" style="font-size:100%;" value="3:00 P.M Weather">
</form>
<form action="" method="post">
	<input type="submit" name="weatherNine" style="font-size:100%;" value="9:00 P.M Weather">
</form>
<form action="" method="post">
	<input type="submit" name="nextWeather" style="font-size:100%;" value="9:00 A.M Tomrrow Weather">
</form>
</div>

<div id="time">
<form action="" method="post">
	<select name="hour" id="hour">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option>
		<option value="8">8</option>
		<option value="9">9</option>
		<option value="10">10</option>
		<option value="11">11</option>
		<option value="12">12</option>
	</select>	
	<select name="minute" id="minute">
		<option value="00">00</option>
		<option value="05">05</option>
		<option value="10">10</option>
		<option value="15">15</option>
		<option value="20">20</option>
		<option value="25">25</option>
		<option value="30">30</option>
		<option value="35">35</option>
		<option value="40">40</option>
		<option value="45">45</option>
		<option value="50">50</option>
		<option value="55">55</option>
	</select>
	<select name="ampm" id="ampm">
		<option value="am">AM</option>
		<option value="pm">PM</option>
	</select>
	<input type="submit" name="settime" value="Set">
</form>
<form action="" method="post">
	<input type="submit" name="alarmOff" value="Alarm Off">
</form>
</div>

</body>
</html>
