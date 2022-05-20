<?php

$options = array( "+", "-", "%");
function functionName($fname) 
{
    exit("geen " . $fname);
}
echo '+ of - of %?' . PHP_EOL;
$str1 = readline();
if (!in_array($str1, $options)) {
    functionName("geldige operatie");
}

echo 'nummer 1?' . PHP_EOL;
$num1 = readline();
if (!is_numeric($num1)) {
    functionName("getal");
}
echo 'nummer 2?' . PHP_EOL;
$num2 = readline();
if (!is_numeric($num2)) {
    functionName("getal");
}

if ($str1 == "+") {
    echo (int)$num1 + (int)$num2;
} else if ($str1 == "-") {
    echo (int)$num1 - (int)$num2;
} else {
    echo (int)$num1 % (int)$num2;
}

?>