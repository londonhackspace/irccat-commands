#!/usr/bin/perl

use POSIX qw(ceil floor);

use Modern::Perl;
use Date::Format;

use lib "/usr/share/irccat/";
use PubStandards::Dates;

my $ps = PubStandards::Dates->new();
my $next = $ps->get_next_pubstandards_date(); 

my $remaining = $next - time;

if ($remaining <= 0) {
    print "Pub Standards is currently in progress! Quick, to the pub! Run!\n";

} else {
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
}

