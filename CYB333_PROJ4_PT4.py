#PART 4)

# Building packets to send google and you can view the RAW packets.

p = IP(dst = 'www.google.com') / TCP(dport = 80) / Raw(b'Raw Data')


#sends packets without custom ether() layer and waits for first answer.
#sr( ) - sends and receives at layer 3. Waits for multiple responses.
#srp( ) - sends and receives packets at layer 2. Waits for multiple responses.
#sr1( ) - sends and receives at layer 3. Only returns the first packet received.
#srp2( ) - sends and receives packets at layer 2. Only returns the first packet received.
#srloop( ) - Sends stimulus, receives responses and displays responses, in a loop.
#The function returns a couple of packet and answers, and the unanswered.

sr1(p)

