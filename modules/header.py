#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import time
import urllib2
import socket
from termcolor import colored, cprint

def head():
	start = colored("header", 'blue')
	
	joker = raw_input(start + "[!] Enter Your Domain >")
	kader = socket.getfqdn(joker)
	hed   = urllib2.urlopen('http://api.hackertarget.com/httpheaders/?q='
		+joker).read().rstrip()
	
	cprint("[*] Please Wait...", 'red')
	time.sleep(1)
	cprint("HTTP Header Domain Lookup", 'green')
	time.sleep(1) 
	print hed 



