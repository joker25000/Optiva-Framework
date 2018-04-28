#! /usr/bin/env python2.7
# code : UltimateHackers
# Modules Optivaframework  


from bs4 import BeautifulSoup
import requests
import mechanize
import sys
from re import search, findall
from urllib import unquote
from HTMLParser import HTMLParser
from termcolor import colored, cprint

class colors():
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

br = mechanize.Browser()
null = []
dorks = []
targets = []
num = ['0', '10', '20','30','40']

def google(dork, number):
    url = 'https://www.google.com/search?q=' + dork + '&start=' + number
    r  = requests.get(url)
    data = r.text
    if 'Our systems have detected unusual traffic from your computer network' in data:
        print "\033[1;31m[-]\033[0m Captcha Detected!"
        google = 'https://www.google.com/search?q=' + dork + '&start=' + number
        url = 'http://source.domania.net/cgi-bin/source.cgi'
        data = requests.post(url, data='url='+google).text
        data = HTMLParser().unescape(data)
        if 'Our systems have detected unusual traffic from your computer network' in data:
            print "\033[1;31m[-]\033[0m Google blocked our IP! Are you mad bro? Take a break."
        match = search(r'url\?q=[^<]*&amp;', data)
        if match:
            clean_link = unquote(unquote(match.group().split('url?q=')[1][:-5]))
            targets.append(clean_link)
        else:
            pass
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all("h3")
    if len(links) == 0:
        pass
    for row in links:
        for link in row.find_all("a"):
            source = (link.get('href'))
            match = search(r'/url\?q=[^<]*&sa=', source)
            if match:
                clean_link = unquote(unquote(match.group().split('/url?q=')[1][:-4]))
                if '=' in clean_link:
                    targets.append(clean_link)
                else:
                    pass
    if len(links) < 10:
        null.append(1)


def get_dorks(page):
    for page in range(int(page)):
        print "\033[1;32m[+]\033[0m Finding dorks on page %i"%(page + 1)
        url = 'https://cxsecurity.com/dorks/' + str(page)
        response = requests.get(url).text
        response = HTMLParser().unescape(response)
        response = unicode(response)        
        matches = findall(r'<B>Dork:</B>[^<]*</font>', response)
        if matches:
            for match in matches:
                try:
                    match = match.replace('<B>Dork:</B>', '').replace('</font>','')
                    dorks.append(match)
                except:
                    pass
    now = datetime.datetime.now()
    filename = ("dorks%i:%i.txt"%(now.hour,now.minute))
    with open(filename, "a") as f:
        for dork in dorks:
            f.write(dork + '\n')
    print '\033[1;32m[+]\033[0m Dorks dumped in %s'% filename

def scan():
    for url in targets:
        try:
            response = requests.get(url + "'", timeout=5).text
            if 'error' in response and 'syntax' in response or 'MySQL' in response:
                print '\033[1;32m[+]\033[0m ' + url + '\033[1;31m .....Vuln'
                vul_targets.append(url)
            else:
                print '\033[1;31m[-]\033[0m ' + url + '\033[1;32m ....No Vuln'
        except:
              pass 


def sdork():
    start = colored("dork", 'blue')
    dork = raw_input(start + '\033[0m [!] Enter Your Dork > ')
    print '\n\033[1;97m[*_*]\033[1;m Searching Sql Injection Vulnerable \n'
    for number in num:
        if len(null) == 0:
            google(dork, number)
        else:
            break
    scan()
