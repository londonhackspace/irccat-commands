#!/usr/bin/php
<?php

    $from = implode(' ', array_slice($argv, 5));
    if (!$from) $from = 'Now';

    if (is_numeric($from)) {
        $unixTime = $from;
    } else {
        $unixTime = strtotime($from);
    }

    if ($unixTime === false) {
        print 'Estoy cargando mi laser? What you say?';

    } else {
        if (is_numeric($from)) {
            print date('r', $unixTime);
        } else {
            print date('r', $unixTime) . " ({$unixTime})";
        }
    }
