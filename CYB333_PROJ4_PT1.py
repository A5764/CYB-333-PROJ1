#PART 1)

# Importing the Scapy Utilities do we can read the file we did in week 2.

from scapy.all import *

pcap_file = "scapy3.pcap"

#The rdpcap fuction reads the contents of thee Pcap file.

packets = rdpcap(pcap_file)

for packet in packets:

#Print the content of the file.

    print(packet.summary())

