#!/usr/bin/php
<?php

date_default_timezone_set('Europe/London');

function getMiddleDay($day, $month, $year) {
    $thisMonth = mktime(0, 0, 0, $month, 1, $year);

    $daysInMonth = date('t', $thisMonth);
    $middleTimestamp = mktime(0, 0, 0, $month, floor($daysInMonth/2), $year);

    $potentials = array();
    foreach (array(2,3) as $i) {
        $timestamp = strtotime("{$i} {$day}", $thisMonth);
        $potentials[abs($timestamp - $middleTimestamp)] = $timestamp;
    }

    ksort($potentials);
    return array_shift($potentials);
}

// Strtotime is dumb when the number of days in the current month is
// larger than the next, so drop back to the 28th to avoid this
$currentTime = mktime();
if (date('j') > 28) {
    $currentTime = mktime(date('H'), date('i'), date('s'), date('n'), 28);
}

$nextMonth = strtotime("0 month", $currentTime);
$timestamp = getMiddleDay(
    'thursday', 
    date('n', $nextMonth), 
    date('Y', $nextMonth)
);


$startTime = strtotime('6pm', $timestamp);
$remaining = $startTime - mktime();


if ($remaining <= -1.4 * 86400) {
    print "Pub Standards is some time next month. Come back when the script's fixed.\n";

} elseif ($remaining < -0.4 * 86400) {
    print "Pub Standards was yesterday, you twit.\n";

} elseif ($remaining < 0) {
    print "Pub Standards is currently in progress! Quick, to the pub! Run!\n";

} else {
    $days = floor($remaining / 86400);
    $remaining -= $days * 86400;

    $hours = floor($remaining / 3600);
    $remaining -= $hours * 3600;

    $minutes = ceil($remaining / 60);

    if ($days > 1) { $d_s="s"; }
    if ($hours > 1) { $h_s="s"; }
    if ($minutes > 1) { $m_s="s"; }

    $date = 'on the ' . date('jS F', $timestamp) . '.';

    if ($days == 0 && $hours == 0) {
        $message = "{$minutes} minute{$m_s} until beer!";
        $date = 'TODAY!';
    } elseif ($days == 0) {
        $message = "Only {$hours} hour{$h_s}, {$minutes} minute{$m_s} until beer!";
        $date = 'TODAY!';
    } else {
        $message = "{$days} day{$d_s} {$hours} hour{$h_s} until beer!";
    }

    print "The next pub standards is {$date} {$message}\n";
}
