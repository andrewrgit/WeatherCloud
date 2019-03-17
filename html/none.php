<?php
try{
	$db = new SQLite3('/var/www/html/led_db');
	$db->exec('UPDATE mode SET status = "none"');
	echo "Changed to none";
}
catch (Exception $e){
	print $e->getMessage();
	echo "If you are seeing this message then you broke it congratulations, contact your boyfriend";
}
?>

