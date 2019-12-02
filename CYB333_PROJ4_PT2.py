#PART 2)

#If you wanted to fileter out the PCAP file for traffic to HTTPS you would them sepcify the following:
from scapy.all import *

def filtering_sample(scapy3): # name is "Pcap file"

    def filter(p): return TCP in p and p[TCP].dport == 443
    packets = rdpcap(name).filter(filter)
    
#There is no HTTP traffic

    for packet in packets:
        print(packet.summary())
print("No HTTPS traffic detected") 
