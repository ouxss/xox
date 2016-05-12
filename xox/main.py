#!/usr/bin/python

import os
import glob
from termcolor import colored
import subprocess
import collections
import sys
import time
import configparser
import loadscripts
import xOxhelp
import traceback
#configuration file

config = configparser.ConfigParser()
confFile = os.getcwd() + '/conf.ini'
reader = config.read(confFile)
version = config['global']['version']
pythonfolder = config['script']['pythonfolder']
commands = config['help']['commands']

#global variables
categorty = ['Files','Network','Web','Wifi']
#currently used script
script = ''

#currently used Category
Cat = ''

#Mapping between categories and file keys
Catsub ={'Network':'-NT.py','Wifi':'-WI.py','Web':'-W.py','Files':'-F.py' }




#Script options
optionlist = config['script']['options'].split(',')

options =  collections.OrderedDict()
parsearg = {}
for el in optionlist:
	d1=el.split(':')
	options[d1[1]]='0'
	parsearg[d1[1]]=d1[0]


def welcome():
	os.system('clear')
	print colored('[+]','white'), colored('Welcome to xOx ','blue')
	print colored("    Version :","blue"),colored(version,'red')
	print ''

def printusedscript(script):

        print colored('[+]','white')+' Script used : ' + colored(script,'yellow')
        print '    Done.'
        print ''
        print colored('[!]','yellow')+ ' Use : "desc" to get the description of the script '
        print ''
        print colored('[!]','yellow')+ ' Use : "get args" to get script arguments '


def scriptnotfound():
                print colored('[-]','red')+' script not found '


def Getscriptname(sc):

         p = subprocess.Popen(['ls', '../MyPythonscripts/'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         out, err = p.communicate()
         if sc in out:
                deb=out.find(sc)
                frm = out[deb:]
                fin=frm.find('.py')
                name=frm[:fin+3]
                name=name.split('-')[0]+'-'+name.split('-')[1]
                name=name.strip(' ')
                return name

         return ''


def getpythonscripts():
	
	python = []

	for el in pythonfiles:
          try:
                if el.split('.')[1]=='py' and el != "__init__.py":
                        python.append(el)


                        if el.split('-')[2]=='NT.py':
                                Scripts['Network'].append(str(el.split('-')[0]+'-'+el.split('-')[1]))
                        if el.split('-')[2]=='W.py':
                                Scripts['Web'].append(str(el.split('-')[0]+'-'+el.split('-')[1]))
                        if el.split('-')[2]=='WI.py':
                                Scripts['Wifi'].append(str(el.split('-')[0]+'-'+el.split('-')[1]))
                        if el.split('-')[2]=='F.py':
                                Scripts['Files'].append(str(el.split('-')[0]+'-'+el.split('-')[1]))


	  except Exception, e :
                #print str(e)
                pass



	print colored('[+]','white')+ ' %d  Python scripts found ' %(len(python))
	print ""

def showcategories():
	 print ''

         print colored(categorty,'yellow')
         print ''
         print colored('[!]','yellow') + ' Select category with : '+colored('use -C <catagory>','yellow')



def usecategory(categ):

	 global Cat

	 if categ in categorty:

                                print colored('[+]','white')+' Category used : ' + colored(cmd.split(' ')[2],'yellow')
                                print '    Done.'
                                print ''
                                print colored('[!]','yellow')+ ' Use : "list" to list scripts included in this category'

                                Cat = categ


         else:
                                print colored('[-]','red')+' categorie not found ' 


def usescript(scri):
	
	global script

	if scri in Scripts[Cat]:

               printusedscript(scri)

               script = scri

        else:
             sc = Getscriptname(cmd.split(' ')[2])

             if sc!='':
             	printusedscript(sc)

                script = sc
             else:

                scriptnotfound()

def showselectedcategory():
	if Cat !='':
       		print colored('[+]','white')+' Selected category : '+colored(Cat,'yellow')
        else:
		print colored('[!]','yellow')+' You have not selected any category yet.'
          

def showselectedscript():
        if script !='':
                print colored('[+]','white')+' Selected script : '+colored(script,'yellow')
        else:
                print colored('[!]','yellow')+' You have not selected any script yet.'

def Unrecognized(arg):

	if arg!='':
		print colored('[-]','red')+' Unrecognized argument : '+ arg
	else:
		print colored('[-]','red')+' Unrecognized argument.'

def listscripts():
	if Cat !='':
        	print ''
                print colored('[+]','white')+' Scripts of '+colored(Cat,'yellow')+' category : '
                print ''

                print colored(Scripts[Cat],'yellow')
                print ''
                print colored('[!]','yellow')+ ' To get a description of a script use : '+colored('desc <Script name>','yellow')
                print colored('[!]','yellow')+ ' Type : '+colored('use -S <Script Name>','yellow')+' to use a script'

        else:
                print colored('[!]','yellow')+' You have not selected any category yet.'


def scriptdescription():

	if Cat !='' and script!='':

        	p = subprocess.Popen(['python', '../MyPythonscripts/'+script+Catsub[Cat],'--gd','desc' ], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                out, err = p.communicate()
                print ''
                print colored('[+]','white') +' Category : '+colored(Cat,'yellow')
                print colored('[+]','white') +' Script : '+colored(script,'yellow')
                print colored('[+]','white') +' Description : '

                print ''
                print out
		print err


        else:
               print colored('[-]','red')+' Make sure to select a category and a script'
               print colored('[!]','yellow')+' Use : '+ colored('"help"','yellow')+' to get commands list'



def getdefaultargs():

	  print ''
	  
	  for el in options.keys():	
		options[el]='0'


	  p = subprocess.Popen(['python', '../MyPythonscripts/'+script+Catsub[Cat],'--ga','getargs' ], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
          out, err = p.communicate()
	
	  res = out.split(',')
	  for el in res:
	  	arg= el.split('=')[1]
		argkey = el.split('=')[0]
	  	data= arg.split(':')
		if data[0]=="yes":
			if options.has_key(argkey):
				options[argkey] = data[1]
				print colored('[+]','white') +' '+argkey+'='+colored(options[argkey],'yellow')

			else:
				Unrecognized(argkey)

def setscriptarg(key,arg):
	   options[key]=arg
           #print colored('[+]','white')+' Done. '
	   showargs()

	

def invalidsyntax():
	 print colored('[-]','red')+' invalid syntax. '
         print colored('[!]','yellow')+ ' use : '+ colored('"help"','yellow') +' to get commands list.'



def showargs():
	for el in options.keys():
        	if options[el]!='0':
			print colored('[+]','white') +' '+el+'='+colored(options[el],'yellow')

def checkscriptloaded():	
	 if Cat=='' or script=='':
              print colored('[-]','red')+' Make sure to select a category and a script'
              print colored('[!]','yellow')+' Use : '+ colored('"help"','yellow')+' to get commands list'
	      return False
	 return True


def runscript():
	
	run=''
        run+='python'
        run+='../MyPythonscripts/'+script+Catsub[Cat]
	
	
	args=['konsole','--noclose','-e','python','../MyPythonscripts/'+script+Catsub[Cat]]

        for el in  options.keys():
        	if options[el] != '0':
                	run+=' '+parsearg[el]+' '+options[el]
                        run = run.strip()
                        run =run.replace('\n','')
		        args.append(parsearg[el])
			args.append(options[el])	
        try:
		#print run
        	#os.system('konsole --noclose -e '+run)
		#args1=['konsole','--noclose','-e','python',' ../MyPythonscripts/',script+Catsub[Cat]]
		#args=args1+args
		
		p = subprocess.Popen(args, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
          	out, err = p.communicate()
		
        except:
              pass
	    
	showargs()


#########################################################
os.system("clear")
welcome()

loadscripts.loadscripts()

#Scripts folder

pythonfiles = os.listdir(pythonfolder)

#list of python scripts
python = []

#Dictionnary representing script list for each category

Scripts={'Files':[],'Network':[],'Web':[],'Wifi':[]}

#Looking for all python scripts
getpythonscripts() 

	
while True:

  try:
	print ''
	cmd = str(raw_input(colored('xOx','blue')+colored('>> ','red')))
	welcome()

	# Show catagories command	
	if cmd.split(' ')[0]=='show':
		if cmd.split(' ')[1]=="categories":
 	               showcategories()
		elif cmd.split(' ')[1]=='args':
			showargs()
	
		elif cmd.split(' ')[1]=="selected":
			if cmd.split(' ')[2]=="category":
				showselectedcategory()
			elif cmd.split(' ')[2]=="script":
				showselectedscript()
			else:
				Unrecognized(cmd.split(' ')[2])
		else:
		
			Unrecognized(cmd.split(' ')[1])

		
	

	# use command
	elif 'use ' in cmd:

		#-C to choose a category
		if cmd.split(' ')[1]=='-C':
			
			usecategory(cmd.split(' ')[2])

		#-S to choose a script
		elif cmd.split(' ')[1]=='-S':
			usescript(cmd.split(' ')[2])

	#list command	

	elif cmd=='list':
		listscripts()


	# desc command

	elif cmd=='desc':
		scriptdescription()


	#get command
	
	elif cmd.split(' ')[0]=='get':
		if cmd.split(' ')[1]=='default':
			if cmd.split(' ')[2]=='args':
				getdefaultargs()
			else:
				Unrecognized(cmd.split(' ')[2])
		else:
			Unrecognized(cmd.split(' ')[1])
        
	#set command                
	elif cmd.split(' ')[0]=='set': 

		
		if checkscriptloaded():
		
			if options.has_key(cmd.split(' ')[1]) and options[cmd.split(' ')[1]]!="0":
				if cmd.split(' ')[2]!='':
					setscriptarg(cmd.split(' ')[1],cmd.split(' ')[2])
				else:
					Unrecognized('')
			else:
				Unrecognized(cmd.split(' ')[1])

		


#m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_iiiiiiiiiiiii:
				

	elif cmd=='run':
                if checkscriptloaded():
			runscript()
	
	elif cmd=="help":
		xOxhelp.gethelp(commands)			
	elif cmd=='exit':
		print colored('[*]','white'),colored('Bye.','yellow')

		sys.exit(0)

	else:
                invalidsyntax()


  except Exception,e:
	traceback.print_exc(file=sys.stdout)
	#print str(e)
	#invalidsyntax()
	pass
	
