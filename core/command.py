#! /usr/bin/env python2.7
# core the Optivaframework  
import os
from termcolor import colored, cprint


def modules():
	print "\n"
	print "\t\033[93m[+] \033[92mOptiva Gathering Modules\033[33m$\033[91m>"
	print "\n"
	print "\033[93mCommand: " + colored("     \t\033[96mDescription")
	print "\033[92mport\t" + colored("     \t\033[91mPort Scanner")
	print "\033[92mwhois\t" + colored("     \t\033[91mDomain Whois Lookup")
	print "\033[92mheader\t" + colored("     \t\033[91mHTTP Header Domain Lookup")
	print "\033[92mreverse\t" + colored("     \t\033[91mReverse IP Domain Lookup")
	print "\033[92miplocator" + colored("    \t\033[91mRetrieve IP Geolocation info")
	print "\n"
	print "\t\033[93m[+] \033[92mOptiva Hash Modules\033[33m$\033[91m>"
	print "\n"
	print "\033[92mmd5\t" + colored("  \t\033[91mMd5 Encode Text")
	print "\033[92msha1\t" + colored("  \t\033[91mSha1 Encode Text")
	print "\033[92mSHA256\t" + colored("  \t\033[91mSHA256 Encode Text")
	print "\033[92mSHA384\t" + colored("  \t\033[91mSHA384 Encode Text")
	print "\033[92mSHA512\t" + colored("  \t\033[91mSHA512 Encode Text")
	print "\n"
	print "\t\033[93m[+] \033[92mOptiva Scanner Modules\033[33m$\033[91m>"
	print "\n"
	print "\033[93mCommand: " + colored("     \t\033[96mDescription")
	print "\033[92msql\t" + colored("  \t\033[91mSQL Injection Scanner")
	print "\033[92mrce\t" + colored("  \t\033[91mRce Remote Code Execution Scanner")
	print "\033[92mxss\t" + colored("  \t\033[91mXss Cros Site Scripting Scanner")
	print "\033[92mdork\t" + colored("  \t\033[91mDork Search SQL Injection Vuln ")
	print "\033[92madmin\t" + colored("  \t\033[91mAdministrator Panel Finder")

def cmd():
	print "\n"
	print "\033[92mCommand: " + colored("     \t\033[96mDescription")
	print "\033[92mhelp " + colored("      \t\033[91mShow This Message")
	print "\033[92mexit " + colored("      \t\033[91mExit The Framework")
	print "\033[92mclear " + colored("     \t\033[91mClear The Terminal")
	print "\033[92mbanner " + colored("    \t\033[91mShow Optiva Banner")
	print "\033[92minfo " + colored("      \t\033[91mComputer And Network Info") 
	print "\033[92mupdate" + colored("    \t\033[91mGet New Version Framework")
	print "\033[92mauthor " + colored("    \t\033[91mAbout Optiva Develepoer")
	print "\033[92mversion " + colored("   \t\033[91mShow Current Version")
	print "\033[92mshow modules " + colored("\t\033[91mList All Modules")

  
