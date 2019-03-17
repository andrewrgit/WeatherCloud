<?php
try{
	$db = new SQLite3('/var/www/html/led_db');
	$db->exec('UPDATE mode SET status = "shutdown"');
	echo "Shutting down Raspberry Pi. Wait 10 seconds after all lights have shut off to unplug power supply. To power on again, unplug power supply and plug back in.";
}
catch (Exception $e){
	print $e->getMessage();
	echo "If you are seeing this message then you broke it congratulations, contact your boyfriend";
}
?>

