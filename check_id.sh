#!/bin/bash
#=======================================================================#
# Author : José Gonçalves						#
# Version : 1.0								#
# Desc : This script is used to scan all probe, and display all id.	#
#=======================================================================#
#===============================================================#
# How to use : 							#
# Usage : check_id.sh [Arg1]					#
# Example : ./check_id.sh 194.38.191.130 			#
# Output :							#
#					1 A34325DSDHHDE4	#
#					2 AAF432AE543243	#
#					...			#
#===============================================================#

# If you change bus master ip, dont forget update this line :
IP_OPT=$1


if test $# = 0 ; then
	echo 'Please use an argument :'
	echo '
#===============================================================#
# How to use :                                                  #
# Usage : probe_scan.sh [Arg1]                                  #
# Example : ./probe_scan.sh 194.38.191.130                      #
# Output :                                                      #
#                                       1 A34325DSDHHDE4        #
#                                       2 AAF432AE543243        #
#                                       ...                     #
#===============================================================#'
	exit 1;
else
	# Web page parsing and deleted master bus ID:
	echo `curl -q "http://$IP_OPT/1Wire/Search.html" 2>/dev/null | sed --silent -e 's/.*<INPUT.*NAME="Address_\(.*\)".*VALUE="\(.*\)".*./\2/p' | sed -e'/9D00000013407027/d'` > scan.tmp
	
	awk -F'[ ]' '{print $0}' scan.tmp | sed -e 's/ /\n/g' | sort -u && rm -rf scan.tmp
fi

# Cleaning files and exit :
unset IP_OPT

exit 0;
