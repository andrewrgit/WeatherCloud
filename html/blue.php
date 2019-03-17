<?php
try{
	$db = new SQLite3('/var/www/html/led_db');
	$db->exec('UPDATE mode SET status = "blue"');
	echo "Changed to blue";
}
catch (Exception $e){
	print $e->getMessage();
	echo "If you are seeing this message then you broke it congratulations, contact your boyfriend";
}
?>

