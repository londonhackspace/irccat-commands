#!/bin/bash
case $( date +%I ) in
	01) DOCTOR='William Hartnell';      N_DOCTOR='Patrick Troughton'     ;;
	02) DOCTOR='Patrick Troughton';     N_DOCTOR='Jon Pertwee'           ;;
	03) DOCTOR='Jon Pertwee';           N_DOCTOR='Tom Baker'             ;;
	04) DOCTOR='Tom Baker';             N_DOCTOR='Peter Davison'         ;;
	05) DOCTOR='Peter Davison';         N_DOCTOR='Colin Baker'           ;;
	06) DOCTOR='Colin Baker';           N_DOCTOR='Sylvester McCoy'       ;;
	07) DOCTOR='Sylvester McCoy';       N_DOCTOR='Paul McGann'           ;;
	08) DOCTOR='Paul McGann';           N_DOCTOR='Christopher Eccleston' ;;
	09) DOCTOR='Christopher Eccleston'; N_DOCTOR='David Tennant'         ;;
	10) DOCTOR='David Tennant';         N_DOCTOR='Matt Smith'            ;;
	11) DOCTOR='Matt Smith';            N_DOCTOR='Peter Capaldi'         ;;
	12) DOCTOR='Peter Capaldi';         N_DOCTOR='William Hartnell'      ;;
esac

MINUTES=$(date +%M)
MINUTES="${MINUTES#0}"
if [[ "${MINUTES}" == "0" ]]; then
	echo "It is currently ${DOCTOR}"
elif [[ "${MINUTES}" == "1" ]]; then
	echo "It is currently 1 minute past ${DOCTOR}"
elif [[ "${MINUTES}" == "15" ]]; then
	echo "It is currently quarter past ${DOCTOR}"
elif [[ "${MINUTES}" == "30" ]]; then
	echo "It is currently half past ${DOCTOR}"
elif [[ "${MINUTES}" == "45" ]]; then
	echo "It is currently quarter to ${DOCTOR}"
elif [[ "${MINUTES}" == "59" ]]; then
	echo "It is currently 1 minute to ${N_DOCTOR}"
elif [[ "${MINUTES}" -lt 30 ]]; then
	echo "It is currently ${MINUTES} minutes past ${DOCTOR}"
elif [[ "${MINUTES}" -gt 30 ]]; then
    MINUTES=$(( 60 - $MINUTES ))
	echo "It is currently ${MINUTES} minutes to ${N_DOCTOR}"
else
    echo "No idea."
fi
