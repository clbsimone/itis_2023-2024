from scapy.all import *

ip_src = "127.0.0.1"
ip_target = "127.0.0.1"

contatore = 1

while True:
    IP1 = IP(src = ip_src, dst = ip_target)
    TCP1 = TCP(dport = 80)
    globalLayer = IP1/TCP1

    send(globalLayer, inter = .001)
    print("pacchetto inviato", contatore)
    contatore = contatore + 1