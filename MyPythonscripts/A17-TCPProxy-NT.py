import sys
import socket
import threading

desc="This module is a proxy, it bind a server in the SrcHost:SrcPort. So you can send the traffic to the proxy (to print ou modify it). The proxy will forward the taffic to the DstHost:DstPort\nThis module take the receivefirst flag to specify if the proxy should initiate the communication with the DstHost"


def GetDesc():
        print desc
def SrcHost():
        print "yes:127.0.0.1"
def SrcPort():
        print "yes:1919"
 
def DstHost():
        print "yes:ND"
def DstPort():
        print "yes:ND"

def ReceiveFirst():
        print "yes:False"


def hexdump(src, length=16):

	result = []
	
	digits = 4 if isinstance(src,unicode) else 2
	for i in xrange(0, len (src), length):
		s = src[i:i+length]	
		hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
		text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
		result.append (b"%04X     %-*s    %s" % (i,length*(digits +1), hexa,text))

	print b'\n'.join(result)


def receive_from(connection):

	bufer =""

	connection.settimeout(40)

	try:
		while True:
			data = connection.recv(4096)
			if not data:
				break
			bufer += data

	except:
		pass

	return bufer

def request_handler(bufer):

	if 'PASS' in bufer:
		print "[+] Password : "+bufer.split("PASS ")[1]

	return bufer

def response_handler(bufer):

	return bufer

def proxy_handler(client_socket, remote_host,remote_port, receive_first):

	remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	remote_socket.connect((remote_host,remote_port))
	
	if receive_first:
	
		remote_buffer = receive_from(remote_socket)
		hexdump(remote_buffer)
		
		remote_bufer = response_handler(remote_buffer)

		if len(remote_buffer):
		
			print "[<==] Sending "+str(len(remote_buffer))+" bytes to localhost."
			client_socket.send(remote_buffer)

	while True:
		
		local_buffer= receive_from(client_socket)
		
		if len(local_buffer):

			print "[==>] Received "+str(len(local_buffer))+" bytes from localhost."
			hexdump(local_buffer)

			local_buffer = request_handler(local_buffer)

			remote_socket.send(local_buffer)
			print "[==>] sent to remote." 

			remote_buffer= receive_from(remote_socket)
			
			if len(remote_buffer):
				
				print "[<==] received "+str(len(remote_buffer))+" bytes from remote."
				hexdump(remote_buffer)

				remote_buffer = response_handler(remote_buffer)

				client_socket.send(remote_buffer)

				print " [<==] send to localhost."

	
		if not len (local_buffer) or not len (remote_buffer):
		
			client_socket.close()
			remote_socket.close()
			print "[*] no more data. Closing connections."
			break		
		

		


def server_loop(local_host,local_port,remote_host,remote_port,receive_first):

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	try:

	  server.bind((local_host,local_port))
	except:
	 
	  print "[!] Failed to listen on " + str(local_host) + ":" + str(local_port)
	  sys.exit(0)

	print "[+] listening on on " + str(local_host) + ":" + str(local_port)

	server.listen(5)
	
	while True:
	
		client_socket,addr= server.accept()
		print "[=>] Received incoming connection from " + str(addr[0])+":"+str(addr[1])
		proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket, remote_host, remote_port, receive_first))
		proxy_thread.start()

def main():
	
	if len(sys.argv)==2 and sys.argv[1]=='desc':
        	GetDesc()
        	sys.exit(0)
    	elif len(sys.argv)==2 and sys.argv[1]=='DstHost':
        	DstHost()
        	sys.exit(0)
    	elif len(sys.argv)==2 and sys.argv[1]=='DstPort':
        	DstPort()
        	sys.exit(0)

	elif len(sys.argv)==2 and sys.argv[1]=='SrcHost':
        	SrcHost()
        	sys.exit(0)
        elif len(sys.argv)==2 and sys.argv[1]=='SrcPort':
        	SrcPort()
        	sys.exit(0)
	elif len(sys.argv)==2 and sys.argv[1]=='receivefirst':
        	ReceiveFirst()
        	sys.exit(0)
    
	elif len(sys.argv[1:])!=5:
	
		print "usage .py [localhost] [localport] [remotehost] [remoteport] [receivefirst]"
		sys.exit(0)

 	else:
	
		local_host = sys.argv[1]
		local_port = int(sys.argv[2])
		remote_host = sys.argv[3]
		remote_port = int(sys.argv[4])
		receive_first = sys.argv[5]

		if "True" in receive_first:
			receive_first= True	
		else:
			receive_firet = False

		server_loop(local_host,local_port,remote_host,remote_port,receive_first)


main()
