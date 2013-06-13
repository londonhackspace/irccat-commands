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

header('Content-Type: text/calendar');
ob_start();

// Google calendar explodes if you indent ical. Seriously.
?>
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//PUBSTANDARDS//PUBCAL 1.0//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Pub Standards
BEGIN:VTIMEZONE
TZID:Europe/London
X-LIC-LOCATION:Europe/London
BEGIN:DAYLIGHT
TZOFFSETFROM:+0000
TZOFFSETTO:+0100
TZNAME:BST
DTSTART:19700329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0000
TZNAME:GMT
DTSTART:19701025T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
<?

// Strtotime is dumb when the number of days in the current month is
// larger than the next, so drop back to the 28th to avoid this
$currentTime = time();
if (date('j') > 28) {
    $currentTime = mktime(date('H'), date('i'), date('s'), date('n'), 28);
}

for ($i = 0; $i < 100; $i++) {
    $nextMonth = strtotime("{$i} month", $currentTime);
    $timestamp = getMiddleDay(
        'thursday', 
        date('n', $nextMonth), 
        date('Y', $nextMonth)
    );

?>
BEGIN:VEVENT
UID:<?=$timestamp?>PS
DTSTAMP:<?=date('Ymd')?>T<?=date('H')?>0000Z
ORGANIZER:beer@pubstandards.co.uk
LOCATION:The Bricklayers Arms\, Gresse Street\, London\, W1
DTSTART:<?=date('Ymd', $timestamp)?>T180000
SUMMARY:Pub Standards
DTEND:<?=date('Ymd', $timestamp)?>T233000
DESCRIPTION:Beer\, lots of beer.
END:VEVENT
<?

}

?>
END:VCALENDAR
<?

# iCal DEMANDS lines end in CRLF. The twat.
$output = ob_get_contents();
ob_end_clean();
print str_replace("\n", "\r\n", $output);
