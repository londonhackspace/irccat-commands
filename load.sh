#!/bin/bash
uptime|sed 's/.*load average: \([^,]*\),.*/\1/'
