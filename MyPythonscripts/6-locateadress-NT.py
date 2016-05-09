#!/usr/bin/python
import pygeoip
import dpkt
import socket
import sys
import os
from ipaddr import Bytes, IPAddress
import Connector

gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')
IPlist=[]

def printrecord(tgt):


      try:	
	rec = gi.record_by_name(tgt)
	#print rec.keys()
	city = rec['city']
	region= rec['region_code']
	codepostal= rec['postal_code']
	country = rec['country_name']
	longt = rec['longitude']
	lat = rec['latitude']
	
	
	print '[*] Target : '+tgt + ' Geo-located.' 
	print '[+] '+str(city)+', '+str(region)+', '+str(codepostal)+', '+str(country)+'.'
	print '[+] '+str(longt)+', '+str(lat)+'.'

	return tgt,longt,lat

      except:

	print "[-] Unregistred"
def printpcap(pcap):

	for (ts, buf) in pcap:
	  try:
		eth = dpkt.ethernet.Ethernet(buf)
		ip = eth.data
		#print ip.src			
		src = socket.inet_ntoa(ip.src)
		#print type (ip.src)
		#print sys.getsizeof(ip.src)
		#print "######################################"
		#print type (src)
		#print sys.getsizeof(src)
		#print "#####################################"
		src = IPAddress(Bytes(ip.src))
		#print type(src)
		#print sys.getsizeof(src)

		dst = socket.inet_ntoa(ip.dst)
		
		print '[+] src : '+str(src)+'--------> dst: '+str(dst)
		printrecord(src)
		print'                     |              '
                print'                     V              '

		printrecord(dst)
		print '_______________________________________________________'
		
	  except:
	 	pass

def retkml(ip,longt,latt):
	
	kml = ('<Placemark>\n'
	       '<name> %s </name>\n'
	       '<Point>\n'
	       '<coordinates>%6f,%6f</coordinates>\n'
               '</Point>\n'
	       '</Placemark>\n'
		)%(ip,longt,latt)
	return (kml)
	    		

kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
kmlfooter= '</Document>\n</kml>\n'


IP,PCAP= Connector.connect("Connector6.ini")

if PCAP!="ND":
	
	f= open(PCAP)
	pcap = dpkt.pcap.Reader(f)
	printpcap(pcap)
else:

	printrecord(IP) 
	#ip,longt,lat = printrecord(IP)
        #kmlpt = retkml(ip,longt,lat)
	#kmldoc=kmlheader+kmlpt+kmlfooter
	#with open ("Onedesti.kml","w") as f:
        #    f.write(kmldoc)

'''
elif len(sys.argv)==3:

        ip,longt,lat = printrecord(sys.argv[1])
        kmlpt = retkml(ip,longt,lat)
        ip2,longt2,lat2 = printrecord(sys.argv[2])
        kmlpt = kmlpt + retkml(ip2,longt2,lat2)
        kmldoc=kmlheader+kmlpt+kmlfooter

        with open ("desti.kml","w") as f:
                f.write(kmldoc) 
'''


#tgt = '173.255.226.98'


#printrecord(tgt)

