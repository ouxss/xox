#!/usr/bin/python

import socket
import threading
import sys
import os
import time
import subprocess
import smtplib


bind_ip = "0.0.0.0"
response = "<!DOCTYPE HTML PUBLIC '-//IETF//DTD HTML 2.0//EN'> <html><head> <meta HTTP-EQUIV='REFRESH' content='0; url=https://127.0.0.1'> <title>404 Not Found</title> </head><body> <h1>Not Found</h1> <p>The requested URL PAGETOREP was not found on this server.</p> <hr> <address>Apache/2.4.7 (Ubuntu) Server at 127.0.0.1 Port 80</address> </body></html>"

responsessh = "SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.6\n"

serverhttp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#serverssh = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
KeepSSH = True
sendnumber = 0
sshnumber = 0

def sendmail(stop):

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("EPHSRP@gmail.com", "kAXF:.<g6yw]dN>+")
 
	msg = str(stop)
	server.sendmail("EPHSRP@gmail.com", "EPHSGRP@gmail.com", msg)
	server.quit()


def StartFssh():

	global KeepSSH	
	global sshnumber
	global sendnumber

	sshnumber=0
	sendnumber=0
	KeepSSH=True
		
	print '[+] Stopping ssh server 0.R'
	os.system('sudo service ssh stop')
	time.sleep(5)

	sshserver = threading.Thread(target=SSHServer)
	sshserver.start()


def ApacheWebServer():

	global sendnumber
	global sshnumber
   	try:
		serverhttp.bind((bind_ip,80))
		serverhttp.listen(5)
		print ('[+] Listening on port 80')
	except Exception, e:

                print '[-] Listen failed : ' +str(e)
                sys.exit(1)
		
	while True:
		try:	
			client,addr = serverhttp.accept()
			print '[*] Accepted connection from : %s:%d' %(addr[0],addr[1])
			request = client.recv(1024)

			try:

			    if '!rcode!' in request:

				try:
				  	print 'send number : ' + str(sendnumber)				
					sendmail(sshnumber-1)
					print 'mail sent' 
					client.send(response.replace('PAGETOREP',request.split(" ")[1]))
                                	client.close()
				
				except Exception, e:

					print str(e)
					client.send(response.replace('PAGETOREP',request.split(" ")[1]))
                                        client.close()


					

			    else:
				
				try:
					number1 = int(request.split(" ")[1].split('$')[0].replace('/','')) 
					number2 = int(request.split(" ")[1].split('$')[1])
					
					

					number = int(number1/number2)
					sendnumber = number +1
					
					if sshnumber!=0:
						print 'ssh number ' + str(sshnumber)
						print 'sendnumber ' + str(sendnumber) 

                                                if sendnumber== sshnumber:

                                                        StartFssh()
					

					client.send(response.replace('PAGETOREP',request.split(" ")[1]))
                                        client.close()
				except Exception, e:
					print str(e) 
					client.send(response.replace('PAGETOREP',request.split(" ")[1]))
					client.close()
			except Exception, e:

				print str(e)
				client.send(response.replace('PAGETOREP',''))
                        	client.close()
		except Exception, e:
			
			print str(e)

			pass
		
def SSHServer():

	global sendnumber
	global KeepSSH
	global sshnumber

	serverssh = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverssh.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	try:

		serverssh.bind((bind_ip,22))
		serverssh.listen(5)
		print ('[+] Listenning on port 22')
	except Exception,e:
		
		print '[-] listen failed ! ' +str(e)
		sys.exit(1)

	while KeepSSH:

		try:
		
			client, addr = serverssh.accept()
			print '[*] Accepted connection from : %s:%d' %(addr[0],addr[1])
			client.send(responsessh)
			request = client.recv(1024)
		
			if '!use:' in request:
				
				number=int(request.split('!use:')[1])
				print number
			
				if number==sendnumber-1:
					
					KeepSSH = False
					print '[+] Stopping SSH server 0.F'
					client.send("Protocol mismatch.\n")
                        		client.close()
					serverssh.close()

					sshnumber=sendnumber
					sendnumber=0
					
					
					time.sleep(5)
					print '[+] Starting SSH server 0.R'
					#os.system("sudo service ssh stop")
					p0 = subprocess.Popen(['sudo','service','ssh','start'])
					p0.wait()
					#os.system("sudo service ssh start")
					#time.sleep(5)
				else:
					client.send("Protocol mismatch.\n")
                        		client.close()
					
					
			elif '!rcode!' in request:
				try:

					sendmail(sendnumber-1)
					print 'mail sent'
					client.send("Protocol mismatch.\n")
                                	client.close()
	
				except Exception, e:
					
					print str(e)
						
					client.send("Protocol mismatch.\n")
                                	client.close()
				
			else:
				client.send("Protocol mismatch.\n")
				client.close()
			
		

		except Exception, e:
			
			print str(e)
			pass
			
			

print '[+] stopping ssh server'
os.system('sudo service ssh stop')
print  '[+] Starting apache web server '

webserver = threading.Thread(target=ApacheWebServer)
webserver.start()

print  '[+] Starting SSH server '

sshserver = threading.Thread(target=SSHServer)
sshserver.start()

