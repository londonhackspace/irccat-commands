#!/bin/bash
clients=$(nmap 172.31.24.0/24 -p1 | grep -c ".dhcp.lan.london.hackspace.org.uk")
echo There are $clients clients connected to the wifi.
