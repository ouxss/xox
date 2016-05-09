import socket
import os

host = "127.0.0.1"
port = 0

if os.name =='nt':
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP


sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
try:
	sniffer.bind((host,port))
except Exception ,e:
	print str(e)

sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

if os.name=="nt":
	sniffer.ioclt(socket.SIO_RCVALL,socket.RCVALL_ON)

print sniffer.recvfrom(65565)

if os.name=="nt":
	sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)


