import sys
import optparse
import configparser
import os


desc ="Module description "
usage ="usage"
confFile =''
config = configparser.ConfigParser()

def checknone(options):
	for el in config['args'].keys():
		if eval("options."+el)==None:
			return True
	return False

def setconf(confile):
	
	global desc
	global usage
	global config
	config = configparser.ConfigParser()
	confFile = '../MyPythonscripts/'+confile
	reader = config.read(confFile)
	desc = config['general']['description']
        usage= config['usage']['usagemsg']	

def getargs():
	argslist= config['args']
	args=""
	i=0
	for el in argslist.keys():
		if i==0:
			 args+=el+'='+argslist[el]
			 i=1
		else:
			args+=','+el+'='+argslist[el]
	
		
        print args


def GetDesc():
        print desc

def connect(confile):

    setconf(confile)
    parser = optparse.OptionParser(usage)
    argslist= config['args']

    for el in argslist.keys():
    	parser.add_option(config['options'][str(el)], dest=str(el), type='string')

    parser.add_option('--ga', dest='args', type='string')
    parser.add_option('--gd', dest='desc', type='string')

    (options, args) = parser.parse_args()

    if options.desc == 'desc':

        GetDesc()
        sys.exit(0)

    elif options.args =='getargs':
        getargs()
        sys.exit(0)

    
    elif checknone(options):
        print parser.usage
        exit(0)
    else:
	ind = 0
	ret=""
	for el in config['args'].keys():
		if ind==0:
			ret+='options.'+el
			ind =1
		else:
			ret+=',options.'+el			
		

        return eval(ret)

