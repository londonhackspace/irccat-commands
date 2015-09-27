#!/bin/bash

echo "There have been `curl http://boole:8001/|wc -l` DHCP leases in the last hour"
