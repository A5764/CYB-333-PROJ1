#PART 5)

#A uselful tool in troubleshooting is the PING command, 

import logging
from scapy.all import *

dstip = raw_input("ENter the IP for an address to test... ")

# Create a basic ICMP Header

icmp = ICMP()
icmp = type=8
icmp.code=0

#Create a basic IP header

ip=IP()
ip.dst=dstip

#Send the data.

p=sr1(ip/icmp,timeout=5,verbose=0)

if(p):
		print "IP is UP"

#Adding the else statement in case the ping failes.
else:
		print "IP is Down"

