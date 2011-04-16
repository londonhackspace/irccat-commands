#!/usr/bin/php
<?php
$args = array_splice($argv, 5);

if (count($args) == 0) {
    $items[] = "heads";
    $items[] = "tails";
} else {
    $string = implode(" ", $args);
    $items = explode(" or ", $string);
    if (count($items) == 1) {
        $items = explode(",", $string);
    }
}

print $items[array_rand($items)];
?>
