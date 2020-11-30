<!doctype html>

<html lang="en">
<head>
	<meta charset="utf-8">

	<title>Home Security and Alarm System - General Settings</title>
	<meta name="description" content="Home Security General Settings Page">
	<meta name="author" content="Todd Bauer, Gerardo Ortiz">

	<link rel="stylesheet" href="styles/settings.css">
	<link rel="stylesheet" href="styles/all.css">
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
	jQuery(document).ready(function(){
		jQuery("#navbar").load("navbar.php");
	});
	</script> 
</head>

<body>
	<div id="navbar"></div>
	
	<div class="wrapper">
		<h2>General Settings</h2>
		<br/>
        <?php 
            $file = "settings.txt";
            $arr_settings = json_decode(file_get_contents($file), true);
        ?>
        <form action="settings_submit.php" method="POST">
            <label for="videolog">Enable Video Logging</label>
            <input type="checkbox" name="videolog" <?php
                if($arr_settings["videolog"]["enabled"] == "on") echo checked;
            ?> />
            <br/><br/>
            
            <label for="videopath"><b>Video Log Path: </b></label>
            <input type="text" name="videopath" value="<?php
                echo $arr_settings["videolog"]["path"];
            ?>" required>
            <br/><br/><hr/><br/>
            
            <label for="motionlog">Enable Motion Logging</label>
            <input type="checkbox" name="motionlog"  <?php
                if($arr_settings["motionlog"]["enabled"] == "on") echo checked;
            ?> />
            <br/><br/>
            
            <label for="motionpath"><b>Motion Log Path: </b></label>
            <input type="text" name="motionpath" value="<?php
                echo $arr_settings["motionlog"]["path"];
            ?>" required>
            <br/><br/><br/><br/>
            
            
            <button type="submit" value="Submit" class="applybutton">
                Apply Settings
            </button>
        </form>
    </div>
</body>
</html>