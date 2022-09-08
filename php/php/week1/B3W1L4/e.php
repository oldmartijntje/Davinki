<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <?php
    echo '<h1>goedemorgen</h1>';
    echo '<h1>het is nu ' . (date("h:i", time())) . '</h1>';
    
    ?>
    <?php if ((int)date("h", time()) >= 6 && (int)date("h", time()) < 12) : ?>
        <html style="background-image: url('morning.png');">
    <?php endif; ?>
    <?php if ((int)date("h", time()) >= 12 && (int)date("h", time()) < 18) : ?>
        <html style="background-image: url('morning.png');">
    <?php endif; ?>
    <?php if ((int)date("h", time()) >= 18) : ?>
        <html style="background-image: url('morning.png');">
    <?php endif; ?>
    <?php if ((int)date("h", time()) < 6) : ?>
        <html style="background-image: url('morning.png');">
    <?php endif; ?>
</body>
