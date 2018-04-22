#! /usr/bin/env python2.7
# Modules Optivaframework  

import os
import sys
import hashlib
from termcolor import colored, cprint

def SHA384hash():
  start = colored("SHA384", 'blue')
  hsh = raw_input (start + '[!] Enter Your Text > \033[92m')
  ho = hashlib.sha384(hsh.encode())
  print ho.hexdigest()
  ext()

