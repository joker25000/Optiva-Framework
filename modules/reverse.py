#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import time
import urllib2
import socket
from termcolor import colored, cprint

def revip():
	start = colored("reverse", 'blue')
	
	joker = raw_input(start + " [!] Enter Your Domain >")
	kader = socket.getfqdn(joker)
	rev   = urllib2.urlopen('http://api.hackertarget.com/reverseiplookup/?q='
		+joker).read().rstrip()
	
	cprint("[*] Please Wait...", 'red')
	time.sleep(1)
	cprint("Reverse IP Domain Lookup", 'green')
	time.sleep(1) 
	print rev 



