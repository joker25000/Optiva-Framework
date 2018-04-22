#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import urllib2
import json
from termcolor import colored, cprint

def iploc():
	start = colored("iplocator", 'blue')
	joker=raw_input(start +"\033[93m [!] Enter Your Domain > ")
	url = "http://ip-api.com/json/"
	reponse = urllib2.urlopen(url + joker)
	name = reponse.read()
	labs = json.loads(name)

	print("\033[92m" + "\n IP: " + labs['query'])
	print("\033[92m" + " Status: " + labs['status'])
	print("\033[92m" + " Region: " + labs['regionName'])
	print("\033[92m" + " Country: " + labs['country'])
	print("\033[92m" + " City: " + labs['city'])
	print("\033[92m" + " ISP: " + labs['isp'])
	print("\033[92m" + " Lat,Lon: " + str(labs['lat']) + "," + str(labs['lon']))
	print("\033[92m" + " ZIPCODE: " + labs['zip'])
	print("\033[92m" + " TimeZone: " + labs['timezone'])
	print("\033[92m" + " AS: " + labs['as'] + "\n")