from Crypto.PublicKey import RSA
from Crypto import Random
import pickle
import socket
import sys
import Connector

###########################

#random_generator = Random.new().read
#key = RSA.generate(1024,random_generator)

host,port,k1,k2=Connector.connect('ConnectorA29.ini')

port= int(port)
key_public = RSA.importKey(open(k1,"rb").read())
key= RSA.importKey(open(k2,"rb").read())
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try: 
	
	client.connect((host,port))
except Exception,e:

	print str(e)
	sys.exit(0)
	
if port==22:
	client.recv(1024)
	
cmd = "GetN"
enc_data = key_public.encrypt(cmd,32)
client.send(enc_data[0])
rep = client.recv(1024)
repe = long(key.decrypt(rep))
repe = str(repe+5)
repc = key_public.encrypt(repe,32)
client.send(repc[0])
print "[+] connection established to %s:%d" %(host,port)

cmd = raw_input('>>')
enc_data = key_public.encrypt(cmd,32)
client.send(enc_data[0])
rep = "fe"
while rep:
	rep =client.recv(1024)
	try:
		print key.decrypt(rep)
	except:
		#rep =client.recv(1024)
		#print key.decrypt(rep)
		pass


	
	


	


#key.decrypt(enc_data)
#print key.decrypt(enc_data)
