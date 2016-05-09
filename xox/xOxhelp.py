#!/usr/bin/python

from termcolor import colored


def error():
	print " [-] syntax error." 
def run():
	print "\n start the current script."

def set():
	print "\n [*] set <argument> <value> : Set a value to a script argument."  

def get():
	print "\nThis command come with several options:\n [*] get default args : to display all the script's argument with their default values." 

def desc():
	print "\nDisplay the description of the current script. "

def listt():
	print "\nTo list all scripts of the current category." 

def use():
	print"\nThis command come with several options:\n [*] use -C <category name> : to select a category.\n [*] use -S <script name> to select a script."
def show():
	print "\nThis command come with several options:\n [*] show categories : to display all scripts categories\n [*] show args : to display the arguments of the current script (you need to call get default arguments first)\n [*] show selected category : to display the selected category.\n [*] show selected script : to display the semected script."
def helpp():
	print "\nHere you are baby :* "
def gethelp(com):
	print colored('[+]','white'), colored('Welcome to xOx help ','blue')
	print colored('[+]','white')+" Disponible commands : "
	commands=com.split(',')
	print ''
	for el in commands:
		print "  [*] "+str(el)	
	print ''
	print colored('[+]','white'), colored('type command name to get a description ','blue')
	print colored('[+]','white'), colored('type exit to return to xOX console ','blue') 

	while True:
		print ''
        	cmd = str(raw_input(colored('xOx','blue')+colored('Help','yellow')+colored('>> ','red')))	

		if cmd=="show":
			show()
		elif cmd=="use":
			use()
		elif cmd=="list":
                        listt()
		elif cmd=="desc":
                        desc()
		elif cmd=="set":
                        set()
		elif cmd=='get':
			get()
		elif cmd=="run":
                        run()
		elif cmd=="help":
                        helpp()
		elif cmd=="exit":
                        return
		else:
			error()
		
		

