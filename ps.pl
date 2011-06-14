#!/usr/bin/perl

use POSIX qw(ceil floor);

use Modern::Perl;
use Date::Format;

use lib "/usr/share/irccat/";
use PubStandards::Dates;

my $ps = PubStandards::Dates->new();

my $now   = time();
my $month = (localtime $now)[4]+1;
my $year  = (localtime $now)[5]+1900;

my $next = $ps->get_middle_thursday_of_month($year, $month); 

my $remaining = $next - time;

if ($remaining <= 0) {
    $month++;
    if ( $month == 13 ){
        $month = 1;
        $year++;
    }
    $next = $ps->get_middle_thursday_of_month($year, $month); 
}

my $d_s = '';
my $h_s = '';

my $days = floor($remaining / 86400);
$remaining -= $days * 86400;

my $hours = floor($remaining / 3600);
$remaining -= $hours * 3600;

my $minutes = ceil($remaining / 60);

if ($days > 1) { $d_s="s"; }
if ($hours > 1) { $h_s="s"; }

my $date = 'on the ' . time2str('%o %B', $next) . '.';
my $message = '';

if ($hours == 0) {
    $message = "$days day" . $d_s . " until beer!";
} elsif ($days == 0) {
    $message = "Only $hours hour" . $h_s . " until beer!";
    $date = 'TODAY!';
} else {
    $message = "$days day" . $d_s . ", $hours hour" . $h_s . " until beer!";
}

print "The next pub standards is $date $message\n";
