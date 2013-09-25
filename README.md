ProbeMgmt
=========

Probe script used by nagios to get temperatures and id.

Usage
=====

check_id.sh
check_temp.sh 
check_temp.py

To get id :
	check_id.sh [bus_ip]
	
output : 
1 A34325DSDHHDE4
2 AAF432AE543243
...

To get all temp :
	check_temp.sh [ProbeID] [Warning_Threeshold] [Critical_Threeshold] [Bus_IP]
	check_temp.py [ProbeID] [Warning_Threeshold] [Critical_Threeshold] [Bus_IP]
	
Normal output :
	"[OK] Temperature: "42"°C | Temperature="42"°C State=Normal"
	
Warning output :
	"[Warning]- Temperature :"35"°C | Temperature="35"°C State=Warning"

Critical output :
	"[Critical]- Temperature : 23°C | Temperature="23"°C State=Critical"

Error output :
	"[Error]- ProbeBus is probably unreacheable. | Temperature=0°C State=Error"
