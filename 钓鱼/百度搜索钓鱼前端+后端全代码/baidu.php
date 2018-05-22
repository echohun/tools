<?php

$wd = urlencode($_REQUEST['wd']);
$log = fopen("baidu_search.txt", "a");
fwrite($log, $wd . "\r\n");
fclose($log);

#echo $wd;

echo '<script language="javascript">';
echo "location.href='https://www.baidu.com/s?wd=".$wd."&rsv_spt=1&rsv_iqid=0xcd9013d50001ba80&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&inputT=805&rsv_sug4=816'";
echo '</script>';


?>
