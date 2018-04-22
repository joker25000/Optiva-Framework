#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import time
import urllib2
import socket
from termcolor import colored, cprint

def port():
	start = colored("port", 'blue')
	joker = raw_input(start + " [!] Enter Your Domain >")
	kader = socket.getfqdn(joker)
	rev   = urllib2.urlopen('http://api.hackertarget.com/nmap/?q='
		+joker).read().rstrip()
	
	cprint("[*] Please Wait...", 'red')
	time.sleep(1)
	cprint("Start Port Scanner", 'green')
	time.sleep(1) 
	print rev 



