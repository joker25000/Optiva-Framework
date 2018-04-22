#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import hashlib
from termcolor import colored, cprint

def md5hash():
  start = colored("md5", 'blue')
  hsh = raw_input (start + '[!] Enter Your Text > \033[92m')
  ho = hashlib.md5(hsh.encode())
  print ho.hexdigest()
  ext()

