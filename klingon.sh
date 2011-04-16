#!/usr/bin/perl

print map { (("A".."Z", "a".."z"), ("'") x 5, (" ") x 8)[rand 65] } 1..(rand 15)+10;
print "\n";
