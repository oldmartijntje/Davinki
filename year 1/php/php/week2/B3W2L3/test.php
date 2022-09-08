<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
	// request method is post
	// now handle the form data

	// declare name and email variables
	$name = $email = '';

	if (empty($_POST['name'])) {
		$nameError = 'Name should be filled';
	} else {
		$name = trim(htmlspecialchars($_POST['name']));
	}

	if (empty($_POST['email'])) {
		$emailError = 'Please add your email';
	} else {
		$email = trim(htmlspecialchars($_POST['name']));
	}
}
?>
<html>
<head>
	<title>PHP Forms</title>
	<style type="text/css">
		.error {
			color:red;
		}
	</style>
</head>
<body>

<form method="POST" action="">
	Name: <input type="text" name="name">
	<span class="error"><?php if (isset($nameError)) {
        echo $nameError; 
                        } ?></span>

	Email: <input type="text" name="email">
	<span class="error"><?php if (isset($emailError)) {
        echo $emailError; 
                        } ?></span>
	<input type="submit" name="submit">
</form>

</body>
</html>
