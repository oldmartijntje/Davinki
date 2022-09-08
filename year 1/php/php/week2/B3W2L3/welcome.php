<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" type="text/css" href="style.css">
    </head>
<body>
    <?php 
    $nameErr = $emailErr = "";
    $name = $email = "";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (empty($_POST["name"])) {
            $nameErr = "Name is required";
        } else {
            $name = test_input($_POST["name"]);
        }
        
        if (empty($_POST["email"])) {
            $emailErr = "Email is required";
        } else {
            $email = test_input($_POST["email"]);
        }
    }
    function test_input($data)
    {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
    ?>
    <?php if ($_SERVER["REQUEST_METHOD"] == "POST") { ?>
        <?php
        echo '<h1>De ingevulde gegevens zijn:</h1>';
        echo 'Naam: ' . htmlspecialchars($_POST['name']);
        echo nl2br("\r\nEmailadres: " . htmlspecialchars($_POST['email']));
        ?>
    <?php } else { ?>
        <form method="post" action="">
            <label for="fname">Name:</label><br>
            <input type="text" id="name" name="name">
            <span class="error">* <?php echo $nameErr;?></span>
            <br><br>
            <label for="email">Mail:</label><br>
            <input type="email" id="email" name="email">
            <span class="error">* <?php echo $emailErr;?></span>
            <br><br>
            <input type="submit">
        </form>
    <?php } ?>
    
    </body>
</html>
