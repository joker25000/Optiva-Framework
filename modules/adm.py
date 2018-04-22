#! /usr/bin/env python2.7
# Modules Optivaframework  

import os, httplib, time
from termcolor import colored, cprint

admin_path = ['admin/','administrator/','admin/login.php','admindir/login.php','admin/login.html','admin/index.html','wp-login.php','admin/admin-login.php','admin_login.php', 'adm.php','login.html','administrator.html','login.html','admin.html','cp.html','adminpanel.php','admin_login.php','cpanel','user_login','admin-area/login.php','admin1/','admin2/','admin3/','admin4/','_admin/','usuarios/',
'usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','webadmin/login.php','webadmin/index.php','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html', 'adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','cpanel']
print

def adminv():
	try:
		start = colored("admin", 'blue')
		joker = raw_input(start+"\033[92m[!] Enter Your Domain \033[91m>")
		sanfor = joker.replace("http://","").rsplit("/",1)[0] 
		situs = sanfor.lower()
		for admin in admin_path:
			admin = admin.replace("\n","")
			admin = "/" + admin
			connection = httplib.HTTPConnection(situs)
			connection.request("GET",admin)
			response = connection.getresponse()
			print "\033[1;97mBrutePanel: \033[91m[\033[92m%s\033[91m]-\033[93m[%s]-\033[91m[%s]" % (admin, response.status, response.reason) 
	except(KeyboardInterrupt,SystemExit):
			raise
	except:
		pass	