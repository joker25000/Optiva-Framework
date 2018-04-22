#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import hashlib
from termcolor import colored, cprint

def SHA256hash():
  start = colored("SHA256", 'blue')
  hsh = raw_input (start + '[!] Enter Your Text > \033[92m')
  ho = hashlib.sha256(hsh.encode())
  print ho.hexdigest()
  ext()

