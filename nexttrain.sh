#!/bin/bash
shift; shift; shift; shift

dir=${1,,}

case "$dir" in
    north)
        dir='highbury\|dalston'
        ;;
    south)
        dir='croydon\|new cross\|crystal'
        ;;
    *)
        #dir=$1
        ;;
esac

/home/ms7821/trains.sh Hoxton|grep -i "$dir"|head -1

