#!/usr/bin/env python
#
# Author  : Joker-Security
# Optiva-framework - Web application scanner
# Twitter: https://twitter.com/SecurityJoker
# Channel ; https://www.youtube.com/c/Professionalhacker25
# FACE Pg : https://facebook.com/kali.linux.pentesting.tutorials


#modules
import os
import sys
import time
import hashlib
import datetime
sys.path.append('core/')
from gost import *
from coder import *
from update import *
from banner import *
from command import *
sys.path.append('modules/')
from hashc import *
from hashk import * 
from hashm import * 
from hashs import *
from hashz import *
from xssy import *
from info import *
from sqldork import *
from adm import *
from who import *
from por import *
from rce import *
from sqll import *
from iplocator import *
from reverse import *
from header import *


try:
	from termcolor import colored, cprint

except ImportError as ie:
	print(str(ie))

def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

class OptivaMain(object):
	   
	   def joker(self):
		__version__ = '1.0.4'
		__author__ = "Joker-Security"
		__Github__ = "https://github.com/joker25000"
		__Twitter__ = "https://twitter.com/SecurityJoker"
		__Channel__ = "https://www.youtube.com/c/Professionalhacker25"
		__Facebook__ = "https://facebook.com/kali.linux.pentesting.tutorials"
		__date__ = datetime.datetime.now()
		__tools__ = "15"

                try:
		    github = raw_input("\n\033[92m[\033[91m0ptiva\033[92m]\033[93m$>")

		    if github == 'exit':
		    	print '\033[1;91mThanks for Usage \033[96mOptivaframework !'
		    	sys.exit(0)

		    if github == 'clear':
			    os.system('clear')
			    Banner()
			    GostBanner()
			    return Optiva.joker()

		    if github == 'version':
		    	os.system('clear')
		    	Banner()
		    	GostBanner()
		        print("\033[41mVersion: " + colored(__version__, 'white'))
		        return Optiva.joker()


		    if github == 'banner':
		         Banner()
		         GostBanner()
		         return Optiva.joker()

		    if github == 'xss':
				 xssvu()
				 return Optiva.joker()

		    if github == 'whois':
		    	 whois()
		    	 return Optiva.joker()

		    if github == 'iplocator':
		         iploc()
		         return Optiva.joker()

		    if github == 'dork':
		         sdork()
		         return Optiva.joker()

		    if github == 'rce':
		    	 rceScan()
		    	 return Optiva.joker()

		    if github == 'sql':
		         sqlvuln()
		         return Optiva.joker()

		    if github == 'info':
		         infor()
		         return Optiva.joker() 

		    if github == 'admin':
		         adminv()
		         return Optiva.joker()

		    if github == 'md5':
		    	 md5hash()
		    	 return Optiva.joker()

		    if github == 'sha1':
				 sha1hash()
				 return Optiva.joker()

		    if github == 'show modules':
			    modules()
			    return Optiva.joker()

		    if github == 'update':
		         Optivaf()
		         return Optiva.joker()


		    if github == 'SHA256':
				 SHA256hash()
				 return Optiva.joker()

		    if github == 'SHA384':
				 SHA384hash()
				 return Optiva.joker()

		    if github == 'SHA512':
				 SHA512hash()
				 return Optiva.joker()

		    if github == 'author':
			    Gostauto()
			    return Optiva.joker()

		    if github == 'help':
		    	cmd()
		    	return Optiva.joker()

		    elif github == 'port':
			    port()
			    return Optiva.joker()

		    elif github == 'reverse':
			    revip()
			    return Optiva.joker()

		    elif github == 'header':
			    head()
			    return Optiva.joker()

                except KeyboardInterrupt:
                        cprint("\n[!] You Press Ctrl + C! To Quit.", 'red')
                        sys.exit(1)

                except:
                        pass

def banner():
    Banner()
    GostBanner()


if __name__ == "__main__":
	Banner()
	GostBanner()
	Optiva = OptivaMain()
	Optiva.joker()
