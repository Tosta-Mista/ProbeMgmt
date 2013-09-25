#!/usr/bin/python
# -*- coding: utf-8 -*-
# [Signature ] =================================
# Name:         probe_script.py
# Purpose:      Get some temperature.
# Author:       jgo
#
# Created:      08.08.2013
# Copyright:    (c) jgo 2013
#===============================================
import re, urllib, sys

if len(sys.argv) < 5:
    print "Need 4 arguments! Please use the following example if you want use this script :)."
    print '''#============================================================#
# Usage : ProbeThis.sh [Arg1] [Arg2] [Arg3] [Arg4]           #
# Example : ./ProbeThis.sh A34325DSDHHDE4                    #
#         You get the temp of the probe named A34325DSDHHDE4 #
#	arg1 => ProbeID					                                   #
#	arg2 => Warning Threshold			                             #
#	arg3 => Critical Threshold			                           #
#	arg4 => Bus IP					                                   #
#============================================================#'''
    sys.exit(3)

# [ Config Vars ] =========
probe_id = sys.argv[1]
warn = sys.argv[2]
critical = sys.argv[3]
bus_ip = sys.argv[4]

# [ Job ] =================
htmlSource = urllib.urlopen('http://'+bus_ip+'/1Wire/ReadTemperature.html?Address_Array='+probe_id).read(200000)
matchObj = re.findall(r'VALUE="(.*?)"',htmlSource,re.M|re.I)

if matchObj != None:
    if float(matchObj[8]) >= float(warn) :
        if float(matchObj[8]) >= float(critical):
            print repr("[Critical]- Temperature :"+matchObj[8]+"°C | Temperature="+matchObj[8]+"°C State=Critical")
            sys.exit(2)
        else:
            print "[Warning]- Temperature :"+matchObj[8]+"°C | Temperature="+matchObj[8]+"°C State=Warning"
            sys.exit(1)
    else:
        print "[OK] Temperature: "+matchObj[8]+"°C | Temperature="+matchObj[8]+"°C State=Normal"
        sys.exit(0)
else:
    print '[Error]- ProbeBus is probably unreacheable. | Temperature=0°C State=Error'
    sys.exit(3)
