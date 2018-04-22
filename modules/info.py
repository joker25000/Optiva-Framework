#! /usr/bin/env python2.7
# Modules Optivaframework  
import os, io, platform, sys, socket
from time import sleep
from urllib2 import urlopen
from termcolor import colored, cprint


def infor():
    start = colored("info", 'blue')
    mac_address = os.popen("cat /sys/class/net/eth0/address").read()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    localaddr = s.getsockname()[0] 
    ipaddr = urlopen('http://ip.42.pl/raw').read()
    def_gw_device = os.popen("route | grep '^default' | grep -o '[^ ]*$'").read()
    print "\033[93m+===========================+"
    print "|\033[91m[+] Mac Address:\033[92m " + mac_address + "\033[93m+--------------------------+"
    print "|\033[91m[+] Local address:\033[94m " + localaddr
    print " \033[93m+--------------------------+"
    print "|\033[91m[+] IP Public :\033[95m" + ipaddr
    print "\033[93m+--------------------------+"
    print "|\033[91m[+] Operating System:\033[96m " + platform.system()
    print "\033[93m+--------------------------+"
    print "|\033[91m[+] System Name:\033[97m " + platform.node()
    print "\033[93m+--------------------------+"
    print "|\033[91m[+] Interface :\033[96m " + def_gw_device + "\033[93m+===========================+"
