import socket
import httplib
import threading

bind_adress = "127.0.0.1"
bind_port = 1919


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

try:
	server.bind((bind_adress,bind_port))
	#server.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	server.listen(5)
	print '[*] Listening on port %d ' %(bind_port)

except Exception, e:

	print str(e)
	exit(0)

while True:

	try:
		client,addr = server.accept()
		print '[+] Accepeted connection from : %s:%d' %(addr[0],addr[1])
		
		request = client.recv(1024)

		print request

	except Exception, e:

		print str(e)
	


