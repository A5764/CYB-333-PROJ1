#PART 3)

# We could also setup our own Scapy specify entries, instead of importing the PCAP file.
#I could change the destination address to multple addresses or mulitple ports if I wanted to. 



src = "192.168.0.2"

dst = "192.168.0.3"

#Set a radom well kown port.

sport = random.randint(1024,65535)

dport = int("443")

