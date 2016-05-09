from scapy.all import *
import sys


def predseq(dst):

	seqnum = 0
	prenum = 0
	diffseq = 0
	deffseqlist=[]
	for x in range(1,30):
		if prenum !=0:
			prenum = seqnum
		pkt = IP (dst=dst)/TCP(dport=513)
		ans = sr1(pkt, verbose=0)
		print prenum
		seqnum = ans.getlayer(TCP).seq
		print seqnum
		diffSeq = seqnum- prenum
		deffseqlist.append(seqnum)
		print "[+] TCP seq diff : "+ str(diffseq)
	i =0
	while i<len(deffseqlist):
		print deffseqlist[i+1]-deffseqlist[i]
		i+=1
		
	return seqnum+diffseq

predseq(sys.argv[1])
