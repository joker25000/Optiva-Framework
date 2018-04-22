#!/usr/bin/env python
#
# Optivaframework  Update Module
# Created By Joker-Security (dev-labs)
import os
import subprocess
from termcolor import colored, cprint

def Optivaf():
	print "\033[91m[\033[92m*\033[91m]\033[92m Updating Optiva-Framework , Please Wait ..." 
	try:
		subprocess.Popen("cd /tmp;git clone https://github.com/joker25000/Optiva-Framework;cp -R Optiva-Framework/ /usr/share;rm -rf /tmp/Optiva-Framework/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	except Exception, e:
		print "\033[92m[\033[91m!\033[92m]\033[91m Update Failed."
		pass

	print "\033[91m[\033[92m*\033[91m]\033[92m Update completed successfully."
if __name__ == "__main__":
	Optivaf()
