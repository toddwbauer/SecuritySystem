<!doctype html>

<html lang="en">
<head>
	<meta charset="utf-8">

	<title>Home Security and Alarm System - Main</title>
	<meta name="description" content="Home Security Main Camera Page">
	<meta name="author" content="Todd Bauer, Gerardo Ortiz">

	<link rel="stylesheet" href="styles/main.css">
	<link rel="stylesheet" href="styles/all.css">
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
	jQuery(document).ready(function(){
		jQuery("#navbar").load("navbar.php");
	});
	</script> 
	<script type="text/javascript">
	jQuery(document).ready(function(){
		jQuery("#videocontainer").load("192.168.0.108:8081");
	});
	</script> 
</head>

<body>
	<div id="navbar"></div>
	
	<div class="wrapper">
		<h2>Video Feed</h2>
		<iframe class="videocontainer" scrolling="no" src="http://192.168.0.108:8081" title="Streaming Video"></iframe>
	</div>
</body>
</html>