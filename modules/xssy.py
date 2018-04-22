#! /usr/bin/env python2.7
# Modules Optivaframework  
import requests
from termcolor import colored, cprint

def xssvu():
    fname = "plugins/xss.txt"
    with open(fname) as f:
        content = f.readlines()
    payloads = [x.strip() for x in content]
    start = colored("xss", 'blue')
    url = raw_input(start+'[!] \033[92mEnter Your Domain \033[91m> ')
    vuln = []
    for payload in payloads:
        payload = payload
        xssurl = url+payload
        r = requests.get(xssurl)
        if payload.lower() in r.text.lower():
            print("\033[91m[\033[93m+\033[91m] \033[91mXSS Vulnerable: \033[92m" +url +payload)
            if(payload not in vuln):
                vuln.append(payload)
        else:
            print "\033[92m[!] Not vulnerable!"

    print "+------------------------+\n" + "\033[93m Xss Available Payloads :\033[92m"+"\033[91m\n+------------------------+" 
    print '\n'.join(vuln) 