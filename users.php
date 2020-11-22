<!doctype html>

<html lang="en">
<head>
	<meta charset="utf-8">

	<title>Home Security and Alarm System - User Management</title>
	<meta name="description" content="Home Security User Management Page">
	<meta name="author" content="Todd Bauer, Gerardo Ortiz">
	
	<link rel="stylesheet" href="users.css">
	<link rel="stylesheet" href="all.css">
	
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
		<h2>User Management</h2>
		<br/>
		
		<form action="settings_page.php" method="post">
			<button type="button" class="userbutton">Add User</button>
			<br/>
		
			<button type="button" class="userbutton">Modify User</button>
			<br/>
		
			<button type="button" class="userbutton">Change Password</button>
			<br/>
		</form>
	</div>
</body>
</html>