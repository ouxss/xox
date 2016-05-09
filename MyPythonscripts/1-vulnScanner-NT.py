#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import os
import sys
import optparse


desc="Scan some known vulnerabities on ports 21,22,25,80,110,443 \nThis script will connect to an adresse IP or a range of adresse, and compare the responses headers with responses included in 'VulnerabilityFile'\nBy default 'VulnerabilityFile' is set to /Files/vuln-banners"

def getargs():
	args="DstHost=yes:ND,DstRange=yes:ND,DictFile=yes:../MyPythonscripts/Files/vuln-banners"
	print args
def GetDesc():
	print desc

def parsing():
    parser = optparse.OptionParser("usage %prog "+\
      "-dh <DstHost> -dr <DstRange> -f file")
    parser.add_option('--gd', dest='desc', type='string',\
      help='description')

    parser.add_option('--ga', dest='args', type='string',\
      help='arguments')
	

    
    parser.add_option('--dh', dest='DstHost', type='string',\
      help='Ip Adresse to scan')
    parser.add_option('--dr', dest='DstRange', type='string',\
      help='IP adresse range')
    parser.add_option('--df', dest='filename', type='string',\
      help='specify vulnerabilities file')
    (options, args) = parser.parse_args()

    if options.desc == 'desc':

	GetDesc()
	sys.exit(0)
	
    elif options.args =='getargs':
	getargs()
	sys.exit(0)
	
    elif (options.DstHost == None) | (options.DstRange == None) | (options.filename == None):
        print parser.usage
        exit(0)
    else:
        DstHost = options.DstHost
        DstRange = options.DstRange
        filename = options.filename
	return DstHost,DstRange,filename
    
    return False	
    

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def checkVulns(banner, filename):

    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+] Server is vulnerable: ' +\
                banner.strip('\n')


def main():
	
    DstHost,DstRange,filename = parsing()


 
    ipadress = DstHost.split(".")[0]+"."+DstHost.split(".")[1]+"."+DstHost.split(".")[2]+"."
    rang1=int(DstRange.split("-")[0])	
    rang2=int(DstRange.split("-")[1])	
    portList = [21,22,25,80,110,443]
    for x in range(rang1, rang2):
        ip = ipadress + str(x)
	print "Scanning : " + ip
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print '[+] ' + ip + ' : ' + banner
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()
