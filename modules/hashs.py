#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import hashlib
from termcolor import colored, cprint

def sha1hash():
    start = colored("sha1", 'red')
    hsh = raw_input('[!] Enter Your Text > \033[92m')
    ho = hashlib.sha1(hsh.encode())
    print ho.hexdigest()
    ext()
