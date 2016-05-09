#/usr/bin/python

from scapy.all import *
from IPy import IP as IPTEST

ttlvalues = []
THRESH = 3

def testttl(pkt):

  try:
      if pkt.haslayer(IP):
 	 ipsrc = pkt.getlayer(IP).src
	 ttl = str(pkt.ttl)
	 #print ipsrc
	 checkttl(ipsrc,ttl)
	 #if '8.8.8.8' in ipsrc:
	 # print '[+] Pkt received from : '+ipsrc+' with TTL : ' + ttl

  except:
     pass


def checkttl(ipsrc,ttl):
    if IPTEST(ipsrc).iptype() == "PRIVATE":
	
	return

    else: 


        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry= 0, timeout =1, verbose = 0)
	ttl2 = pkt.ttl
	
      
        res= abs(int(ttl) - int(ttl2)) 
	if res > THRESH:
   	 print '[+] Detection possible spoofed packet from : '+ipsrc
         print '[!] TTL of packet : '+str(ttl)+ ' Tested ttl : '+ str(ttl2)

sniff(prn=testttl,store=0) 
