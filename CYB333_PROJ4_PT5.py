#PART 5)

#A uselful tool in troubleshooting is the PING command, 

import logging
import os
import sys
from scapy.all import *

conf.verb = 0

dstip = input ("ENter the IP for an address to test... ")

for i in range(1,2):
	ip = dstip
	#Sending IP request to the destination IP
	request = IP(dst=ip,ttl=10)/ICMP()
	
	#Sending request with timeout value.
	reply = sr1(request,timeout=2)

	#If the host is down it will be the first if resonse.
	if (reply is None):
		print(ip + " is Down")
	else:
		print(ip + " is Up")

