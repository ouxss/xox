from scapy.all import *


def snifingtcp(pkt):

  try:
     if pkt.haslayer(IP):
         ipsrc=pkt.getlayer(IP).src
	 ipdst=pkt.getlayer(IP).dst
	
         
         if((ipsrc=="192.168.0.118" and ipdst== "192.168.0.106") or (ipsrc=="192.168.0.106" and ipdst=="192.168.0.118") or (ipsrc == "192.168.0.118" and ipdst == "192.168.0.1") or (ipsrc=="192.168.0.1" and ipdst=="192.168.0.118") or (ipsrc=="192.168.0.106" and ipdst=="192.168.0.1") or (ipsrc=="192.168.0.1" and ipdst=="192.168.0.106")): 

		print str(ipsrc) + " ----> "+str(ipdst)
		#if ipsrc=="192.168.0.118" and ipdst=="192.168.0.1":
		if pkt.haslayer(TCP):
			print "seq : " + str(pkt.getlayer(TCP).seq)
			try :
				print "ack : " + str (pkt.getlayer(TCP).ack)
			except :
				pass
		else:
		  print pkt.haslayer(TCP)

			

  except:
	pass


  		
sniff(prn=snifingtcp,store=0)

