<?php

echo '+ of -?' . PHP_EOL;
$str1 = readline();
echo 'nummer 1?' . PHP_EOL;
(int)$num1 = readline();
echo 'nummer 2?' . PHP_EOL;
(int)$num2 = readline();
if ($str1 == "+") {
    echo $num1 + $num2;
} else {
    echo $num1 - $num2;
}

?>