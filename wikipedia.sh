#!/bin/bash
# props to dg, he did all the hard work. i just scripted it

cmd=dig
params="+short txt"
shift; shift; shift; shift;
query=$(echo $* | sed -e 's/ /_/g').wp.dg.cx

# echo $cmd $params $query 
echo $($cmd $params $query)
