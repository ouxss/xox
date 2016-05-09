from scapy.all import *


hiddennets=[]
unhiddennets=[]
show =[]
def sniffdot11(p):

	if p.haslayer(Dot11ProbeResp):
	
	  addr2 = p.getlayer(Dot11).addr2
	  if (addr2 in hiddennets) & (addr2 not in unhiddennets):
	    netName = p.getlayer(Dot11ProbeResp).info
	    print '[+] Decloaked hidden SSID : ' + netName + 'for mac : ' + addr2
	    unhiddennets.append(addr2)
	
	if p.haslayer(Dot11Beacon):
	  if p.getlayer(Dot11Beacon).info=='':
		addr2 = p.getlayer(Dot11).addr2
		if addr2 not in hiddennets:
			print '[-] Detected hidden SSID : ' + addr2
			hiddennets.append(addr2)
	'''  
	else:
	    if p.getlayer(Dot11Beacon).info not in show:
		print '[-] disponible SSID : ' + p.getlayer(Dot11Beacon).info
		show.append(p.getlayer(Dot11Beacon).info)

	'''


sniff (iface='mon0', prn=sniffdot11)
