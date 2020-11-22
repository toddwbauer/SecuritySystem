<?php

    $file = "settings.txt";

    try {
        //$arr_settings = json_decode(file_get_contents($file), true);

        $arr_settings["videolog"] = array("enabled" => $_POST["videolog"], "path" => $_POST["videopath"]);
        $arr_settings["motionlog"] = array("enabled" => $_POST["motionlog"], "path" => $_POST["motionpath"]);
        $arr_settings["activitylog"] = array("enabled" => $_POST["activitylog"], "path" => $_POST["activitypath"]);

        $jsondata = json_encode($arr_settings, JSON_PRETTY_PRINT);


        if (file_put_contents($file, $jsondata)) {
            include("settings.php");
            ?> <div class="wrapper" style="margin-top:20px; padding-top:40px; font-size:30px"> <?php
            echo 'Data successfully saved';
        } else {
            echo "Error: Data could not be saved";
        }
        ?></div><?php
    }
    catch (Exception $e) {
        echo 'Caught exception: ',  $e->getMessage(), "\n";
    }
    







    // Execute the python script with the JSON data
    // $result = shell_exec('python settings_test.py ' . escapeshellarg(json_encode($data)));

    // Decode the result
    // $resultData = json_decode($result, true);

    // This will contain: array('status' => 'Yes!')
    // var_dump($resultData); 
?>




