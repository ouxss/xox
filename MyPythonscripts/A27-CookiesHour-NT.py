from scapy.all import *
import sys
import optparse

desc ="This module sniff the network depends of the selected interface, and show the http request containing cookies\n you can desable the port filter by affecting 'ND' to DstPort\nYou can also dont use the Keyword field by setting it to 'ND'\nIf you dont want save the resulats to a file, let the SaveFile field to 'ND' "
def getargs():
        args="interface=yes:eth0,DstPort=yes:80,keywd=yes:ND,saveonfile=yes:ND"
	print args


keyword='ND'

def GetDesc():
        print desc


def parsing():
    parser = optparse.OptionParser("usage %prog "+\
      "-i <interface> --dp <DstPort> --kw <keywd> --sf file")
    parser.add_option('--gd', dest='desc', type='string',\
      help='description')

    parser.add_option('--ga', dest='args', type='string',\
      help='arguments')



    parser.add_option('-i', dest='interface', type='string',\
      help='interface')
    parser.add_option('--dp', dest='DstPort', type='string',\
      help='Port to sniff')
    parser.add_option('--kw', dest='keywd', type='string',\
      help='Keywork')
    parser.add_option('--sf', dest='saveonfile', type='string',\
      help='file to save results')
	
    (options, args) = parser.parse_args()

    if options.desc == 'desc':

        GetDesc()
        sys.exit(0)

    elif options.args =='getargs':
        getargs()
        sys.exit(0)

    elif (options.interface == None) | (options.DstPort == None)  :
        print parser.usage
        exit(0)
    else:
	
        interface = options.interface
        DstPort = options.DstPort
	keyword = options.keywd
	filename = options.saveonfile
	
        return interface,DstPort,keyword,filename



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


	
interface,Dstport,keyword,saveinfile=parsing()

	
if Dstport!="ND":
	sniff(iface=interface, prn=CookieAnalysei, filter="tcp port "+str(Dstport))
else:
	sniff(iface=interface, prn=CookieAnalysei)



