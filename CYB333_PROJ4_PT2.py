#PART 2)

#If you wanted to fileter out the PCAP file for traffic to HTTPS you would them sepcify the following:


def filtering_sample(scapy3.pcap): # name is "XXX.pcap"

    def filter(p): return TCP in p and p[TCP].dport == 443
    packets = rdpcap(name).filter(filter)

    for packet in packets:
        print(packet.summary())
