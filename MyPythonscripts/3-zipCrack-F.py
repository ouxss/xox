#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import optparse
from threading import Thread
import sys

desc="This module brute force a zip file to get a password.\nIt contains a default dictionnary file on /Files/passwords.txt"

found = False

def GetDesc():
        print desc
def DictFile():
        print "yes:../MyPythonscripts/Files/passwords.txt"
def InFile():
        print "yes:ND"



def extractFile(zFile, password):
    global found
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password ' + password + '\n'
	#return password
	found = True
    except:
	print str(password)
        pass
	


def main():

    global found

    if len(sys.argv)==2 and sys.argv[1]=='desc':
        GetDesc()
        sys.exit(0)
    if len(sys.argv)==2 and sys.argv[1]=='DictFile':
	DictFile()
        sys.exit(0)
    elif len(sys.argv)==2 and sys.argv[1]=='InFile':
	InFile()
        sys.exit(0)
    elif len(sys.argv)==3:
	dname = sys.argv[1]
	zname = sys.argv[2]
    else:
	print "usage %prog <dictionary> <zipfile>"
	sys.exit(0)
    '''	
    parser = optparse.OptionParser("usage %prog "+\
      "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    '''
    print 'Start'
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
	if found:
		sys.exit(0)


if __name__ == '__main__':
    main()
