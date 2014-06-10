#!/usr/bin/python
# -*- coding: utf-8 -*-
# [Signature ] =================================
# Name:         probe_script.py
# Purpose:      Get some temperature.
# Author:       jgo
#
# Created:      08.08.2013
# Copyright:    (c) jgo 2013
# Licence:      <GPL>
#===============================================
import re, urllib, sys, os


def help():
    """
    Function:: help()
    Return:: Returns a message to help the user.
    """
    print "Need 4 arguments! Please use the following example if you want use this script :)."
    print '''#============================================================#
# Usage : ProbeThis.sh [Arg1] [Arg2] [Arg3] [Arg4]           #
# Example : ./ProbeThis.sh A34325DSDHHDE4                    #
#         You get the temp of the probe named A34325DSDHHDE4 #
#   arg1 => ProbeID                                          #
#   arg2 => Warning Threshold                                #
#   arg3 => Critical Threshold                               #
#   arg4 => Bus IP                                           #
#                                                            #
#   OR                                                       #
#   test (Running test using hardcoded data)                 #
#   -h / help To display this message                        #
#                                                            #
#============================================================#'''
    return sys.exit(3)


# [ Testing job ] =========
def test_job():
    """
    Function:: test_job()
    Return:: Return some test using hardcoded data
    """
    test_probe_id = "6400000308730828"
    test_warn = (100, 10, 10)
    test_crit = (200, 200, 10)
    test_bus_ip = "10.10.61.3"

    # Testing normal state :
    test_htmlSource = urllib.urlopen('http://'+test_bus_ip+'/1Wire/ReadTemperature.html?Address_Array='+test_probe_id).read(200000)
    test_matchObj = re.findall(r'VALUE="(.*?)"',test_htmlSource,re.M|re.I)
    
    for (i_warn, i_crit) in zip(test_warn, test_crit):
        if test_matchObj != None:
            if float(test_matchObj[8]) >= float(i_warn) :
                if float(test_matchObj[8]) >= float(i_crit):
                    print "[ Critical State ]"
                    print "[Critical]- Temperature :"+test_matchObj[8]+"°C | Temp="+test_matchObj[8]+"°C State=Critical"
                    print "[Err. Code] Exit code 2 \n"
                else:
                    print "[ Warning State ]"
                    print "[Warning]- Temperature :"+test_matchObj[8]+"°C | Temp="+test_matchObj[8]+"°C State=Warning"
                    print "[Err. Code] Exit code 1 \n"
            else:
                print "[ Normal State ]"
                print "[OK]- Temperature: "+test_matchObj[8]+"°C | Temp="+test_matchObj[8]+"°C State=Normal"
                print "[Err. Code] Exit code 0 \n"
        else:
            print "[ Error ]"
            print "[Error]- ProbeBus is probably unreacheable. | Temp=0°C State=Error"
            print "[Err. Code] Exit code 3 \n"
    return sys.exit(0)

def job(arg1, arg2, arg3, arg4):
    """
    Function:: job(arg1, arg2, arg3, arg4)
    arg1:: Probe ID
    arg2:: Warning Threshold
    arg3:: Critical Threshold
    arg4:: Bus IP address
    Return:: Returns the output format and the correct error code for centreon.
    """
    htmlSource = urllib.urlopen('http://'+bus_ip+'/1Wire/ReadTemperature.html?Address_Array='+probe_id).read(200000)
    matchObj = re.findall(r'VALUE="(.*?)"',htmlSource,re.M|re.I)


    if matchObj != None:
        if float(matchObj[8]) >= float(warn) :
            if float(matchObj[8]) >= float(crit):
                print "[Critical]- Temperature :"+matchObj[8]+"°C | Temp="+matchObj[8]+"°C State=Critical"
                sys.exit(2)
            else:
                print "[Warning]- Temperature :"+matchObj[8]+"°C | Temp="+matchObj[8]+"°C State=Warning"
                sys.exit(1)
        else:
            print "[OK]- Temperature: "+matchObj[8]+"°C | Temp="+matchObj[8]+"°C State=Normal"
            sys.exit(0)
    else:
        print "[Error]- ProbeBus is probably unreacheable. | Temp=0°C State=Error"
        sys.exit(3)



if len(sys.argv) <= 1:
    help()

if sys.argv[1] == "test":
    test_job()
elif sys.argv[1] == "-h" or sys.argv[1] == "help" or sys.argv[1] == "--help":
    help()

# [ Config Vars ] =========
probe_id = sys.argv[1]
warn = sys.argv[2]
crit = sys.argv[3]
bus_ip = sys.argv[4]


# [ Job ] =================
try:
    job(probe_id, warn, crit, bus_ip)
except:
    sys.exit(sys.exc_info()[1])
