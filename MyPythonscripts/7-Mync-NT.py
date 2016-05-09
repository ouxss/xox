#/usr/bin/python


import socket
import sys

#socket.settimeout(1)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5)
ip  = str(sys.argv[1])
port =int( sys.argv[2])

s.connect((ip,port))

while (1):
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((ip,port))
  request = str(raw_input())
#s.send(request)
  Request = "GET / HTTP/1.1\r\nConnection: Close\r\n\r\n"
#Request+= "Host: www.google.fr\r\n"
#Request+= "Connection: Close\r\n\r\n"
  request = request + "Connection: Close\r\n\r\n"
#print Request
#print request
  #print request
  s.send(request)
#print request
  rep = "reponse : "
  while (rep!=""): 
	print rep
        rep = s.recv(5024)
  s.close()
