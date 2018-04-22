#! /usr/bin/env python2.7
# Modules Optivaframework  
import re
import urllib
from vuln import *
from termcolor import colored, cprint

def rceScan():
	start = colored("rce", 'red')
	url = raw_input(start + " [!] Enter Your Domain > ")
	if "?" in url:
		rcevuln(url)
	else:
		print "\n [Warning] "+"%s"%url+" is not a valid URL"
		print " [Warning] You should write a Full URL .e.g http://site.com/index.php?id=value \n"
		exit()			





