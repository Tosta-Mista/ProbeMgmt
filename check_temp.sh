#!/bin/bash

#=======================================================================#
# Author : Jose Goncalves                                               #
# Version : 1.0                                                         #
# Desc : Probe script (Part two). With this script you can get the temp #
#        of the probe, use "args" to get the bus id Temp.               #
#=======================================================================#
#============================================================#
# Usage : ProbeThis.sh [Arg1] [Arg2] [Arg3] [Arg4]           #
# Example : ./ProbeThis.sh A34325DSDHHDE4                    #
#         You get the temp of the probe named A34325DSDHHDE4 #
#       arg1 => ProbeID                                      #
#       arg2 => Warning Threshold                            #
#       arg3 => Critical Threshold                           #
#       arg4 => Bus IP                                       #
#============================================================#

# Init all variables :
ARG=$1
ARG1=$2
ARG2=$3
IP_ADDR=$4
VALUE=`curl -q "http://$IP_ADDR/1Wire/ReadTemperature.html?Address_Array=$ARG" 2>/dev/null | grep $ARG | awk '{print $13;}' | sed --silent -e 's/.*VALUE="\(.*\)".*./\1/p'`
EXIT_CODE=0

# Now it's time to work :
if test $# != 4 ;then
        echo 'Error : Please use an argument.'
        echo '
#============================================================#
# Usage : ProbeThis.sh [Arg1] [Arg2] [Arg3] [Arg4]           #
# Example : ./ProbeThis.sh A34325DSDHHDE4                    #
#         You get the temp of the probe named A34325DSDHHDE4 #
#	arg1 => ProbeID					     					 #
#	arg2 => Warning Threshold			     				 #
#	arg3 => Critical Threshold			      				 #
#	arg4 => Bus IP					     					 #
#============================================================#'
        EXIT_CODE=3
else
	if (( $(echo "$VALUE $ARG2" | awk '{print ($1 >= $2)}') )); then
		echo '[Critical] Temperature: '$VALUE' | Temp='$VALUE' State=Critical'
		EXIT_CODE=2
	else
		if (( $(echo "$VALUE $ARG1" | awk '{print ($1 >= $2)}') )) ; then
			echo '[Warning] Temperature: '$VALUE' | Temp='$VALUE' State=Warning'
			EXIT_CODE=1
		else
			echo '[Ok] Temperature: '$VALUE' | Temp='$VALUE' State=Normal'
			EXIT_CODE=0
		fi
	fi
fi

## Cleaning :
unset IP_ADDR
unset ARG
unset ARG1
unset ARG2
unset VALUE

exit $EXIT_CODE;
