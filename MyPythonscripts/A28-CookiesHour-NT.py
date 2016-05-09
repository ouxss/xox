from scapy.all import *
import sys
import optparse
import Connector

keyword='ND'


def CookieAnalysei(packet):
	global keyword
	keyb=''
	if keyword!="ND":
		keyb=keyword

	http_packet = str(packet)
	ret= '----------------------Packet :--------------------------------------\n'
	ret+='\n'.join(packet.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
	ret+='\n--------------------------------------------------------------------'
	if 'cookie' in ret and keyb in ret:
		 if "Content-Type" in ret or "Date:" in ret or "Expires:" in ret or "Cache-Control:" in ret or "Last-Modified:" in ret or "X-Content-Type-Options:" in ret or "Server:" in ret or "Accept:" in ret or "User-Agent:" in ret or "Referer:" in ret:
			print ret


	
interface,Dstport,keyword,saveinfile=Connector.connect("ConnectorA28.ini")

	
if Dstport!="ND":
	sniff(iface=interface, prn=CookieAnalysei, filter="tcp port "+str(Dstport))
else:
	sniff(iface=interface, prn=CookieAnalysei)



