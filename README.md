ProbeMgmt
=========

Probe script used by nagios to get temperatures and id.

Usage
=====
* check_id.sh
* check_temp.sh
* check_temp.py

To get id :
-----------
	check_id.sh [bus_ip]

<dl>
<dt>output :</dt>
</dl>	
	1 A34325DSDHHDE4
	2 AAF432AE543243
	...
	

To get temp :
-------------
	check_temp.sh [ProbeID] [Warning_Threeshold] [Critical_Threeshold] [Bus_IP]
	check_temp.py [ProbeID] [Warning_Threeshold] [Critical_Threeshold] [Bus_IP]

<dl>
<dt>Normal output :</dt>
	<dd>"[OK] Temperature: "42"°C | Temperature="42"°C State=Normal"</dd>
<dt>Warning output :</dt>
	<dd>"[Warning]- Temperature :"35"°C | Temperature="35"°C State=Warning"</dd>
<dt>Critical output :</dt>
	<dd>"[Critical]- Temperature : 23°C | Temperature="23"°C State=Critical"</dd>
<dt>Error output :</dt>
	<dd>"[Error]- ProbeBus is probably unreacheable. | Temperature=0°C State=Error"</dd>
</dl>
