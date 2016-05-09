import pexpect

PROMPT=['# ', '>>> ', '> ', '\$ ']


def send_command(child,cmd): 
    PROMPT=['# ', '>>> ', '> ', '\$ ']
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user,host,password):
	
	ssh_newkey = "Are you sure you want to continue connecting"
        connStr = 'ssh '+ user +'@'+host
	child = pexpect.spawn (connStr)
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
	if ret==0:
	   print "[-] Timeout "
	elif ret==1:
          child.sendline('yes')
          ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
	  if ret ==1:
	    child.sendline(password)
	    child.expect(PROMPT)
	elif ret==2:
	  child.sendline(password)
	  child.expect(PROMPT) 
	return child
	     


child = connect("cds4","192.168.0.114","EP321*+sAV5!$%cds2300^")
send_command(child,'pwd')

