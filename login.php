<!doctype html>

<html lang="en">
<head>
	<meta charset="utf-8">

	<title>Home Security and Alarm System - Login</title>
	<meta name="description" content="Home Security Login Page">
	<meta name="author" content="Todd Bauer, Gerardo Ortiz">

	<link rel="stylesheet" href="styles/login.css">
	<link rel="stylesheet" href="styles/all.css">
</head>

<body>
	<form action="login_page.php" method="post">
		<div class="wrapper">
			<div class="imgcontainer">
				<img src="shield.png" alt="Avatar" class="avatar">
			</div>

			<div class="logintext">
				<label for="uname"><b>Username</b></label>
				<input type="text" placeholder="Enter Username" name="uname" required>
				<br/><br/>

				<label for="psw"><b>Password</b></label>
				<input type="password" placeholder="Enter Password  " name="psw" required>
				<br/><br/>

				<div class="forgotpassword">
					<span class="psw"><a href="#">Forgot Username/Password</a></span>
				</div>
				<br/>
				
				<button type="submit" class="loginbutton">Login</button>
			</div>
		  
		</div>
	</form>
</body>
</html>