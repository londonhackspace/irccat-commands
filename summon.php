#!/usr/bin/php
<?php

    $args = array_splice($argv, 5);

    $src = file('http://images.google.co.uk/images?q='.urlencode(implode(' ', $args)));
    preg_match('/imgurl\\\x3d(.*?)\\\x26/', implode('', $src), $matches);

    if (!$matches) {
        print "UNKNOWN THING\n";
    } else {
        print "SUMMONED ".strtoupper(implode(' ', $args)).": ".trim($matches[1])."\n";
    }
