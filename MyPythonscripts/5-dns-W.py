#/usr/bin/python

import dpkt
from scapy.all import *
import sys
import pprint
dnsrecord= {}
cmb=0

def handlepkt(pkt):
  
  if pkt.haslayer(DNSRR):
      rrname = pkt.getlayer(DNSRR).rrname
      rdata = pkt.getlayer(DNSRR).rdata

      if dnsrecord.has_key(rrname):
	dnsrecord[rrname].append(rdata)
      else:
       dnsrecord[rrname]=[]
       dnsrecord[rrname].append(rdata)
  if pkt.haslayer(TCP):
      pass:
      #pprint.pprint (vars(pkt.getlayer(TCP)))
      #print pkt.getlayer(TCP).payload
def handlepkt2(pkt,nbr):
 
  '''
  -------------------------------- ETH ----------------------------
{'ip': IP(src='A7\xb9\x1a', dst='\xc0\xa8\xf2\x83', sum=27217, len=163, p=6, ttl=128, id=8838, data=TCP(seq=930119380, ack=4006136096, win=64240, sum=3631, flags=24, dport=1402, sport=80, data='HTTP/1.1 304 Not Modified\r\nDate: Sat, 13 Feb 2010 14:24:44 GMT\r\nEtag: "0e83fe39b6fc91:0"\r\nCache-Control: max-age=604800\r\n\r\n'))}
---------------------------------ip-----------------------------
  '''
  try:  
    eth = dpkt.ethernet.Ethernet(pkt)
    ip = eth.data
    
    trans = ip.data
    payload = trans.data

    #if "go.microsoft.com" in payload:
    # print "yes"
    
  except:
   pass

  if 'payload' in locals():
     #print payload
     if  "HTTP" in payload:
     #if payload == str:
       try:
          http= dpkt.http.Request(payload)
          
       except:
         pass

       if 'http' in locals():
          pprint.pprint (vars(http))


          print '-----------------'
   
     else:

         if "whatsrunning.net".encode('hex') in payload.encode('hex'):
            print "yep"  


  '''

{'body': '',
 'data': '',
 'headers': {'accept': '*/*',
             'accept-encoding': 'gzip, deflate',
             'accept-language': 'en-us',
             'connection': 'Keep-Alive',
             'cookie': 'MC1=GUID=0ac3978173d58a4682d10ea5bb44625c&HASH=8197&LV=20101&V=3; A=I&I=AxUFAAAAAAByBwAAo9zzsjBEmPt1NimuMXPWnw!!&CS=1357{A0001602090216020902h60209; s_nr=1264587597828; s_vnum=1267179597531%26vn%3D1; WT_FPC=id=76.100.201.123-1281380000.30056250:lv=1265731993296:ss=1265730256593; omniID=56988529_7436_4959_9b4b_41c8a98312fc; WT_NVR_RU=0=technet:1=:2=',
             'host': 'www.update.microsoft.com',
             'if-modified-since': 'Tue, 06 Jan 2009 01:12:46 GMT',
             'if-none-match': '"0bbee29b6fc91:0"',
             'referer': 'http://www.update.microsoft.com/microsoftupdate/v6/splash.aspx?page=0&ln=en-us',
             'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)'},
 'method': 'GET',
 'uri': '/microsoftupdate/v6/shared/css/content.css',
 'version': '1.1'}

  '''



  '''
  try:
   print '-------------------------------- ETH ----------------------------'
   #print socket.inet_ntoa(eth.src)
   pprint.pprint (vars(eth))
   
   print '---------------------------------ip-----------------------------'
   pprint.pprint (vars(ip))
   print '--------------------------------trs-------------------------------'  
   pprint.pprint(vars(transport))
   print '-------------------------------trsdata---------------------------------'
   print transport.data
  except:
   
   pass
  '''
  '''
  nbr+=1
  if nbr==10:
     exit(0)
  '''
  ''' 
  try:
     payload = transport.data
   
     print payload
   except:
     pass
   #if "DNSRR" in str(ip):
   #  print "yes"
  
  ''' 



pkts= rdpcap(sys.argv[1])
for pkt in pkts:
 handlepkt(pkt)

'''
f= open(sys.argv[1])
pkts = dpkt.pcap.Reader(f)
#printpcap(pcap)
for ts,pkt in pkts:

  handlepkt2(pkt,cmb)
''' 

for el in dnsrecord.keys():

  print "[+] "+str(el) +" has "+str(len(dnsrecord[el])) + " : " + str(dnsrecord[el])
