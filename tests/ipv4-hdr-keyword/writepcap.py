#!/usr/bin/env python
from scapy.all import *

pkts = []

pkts += Ether(dst='ff:ff:ff:ff:ff:ff', src='00:01:02:03:04:05')/ \
    Dot1Q(vlan=6)/ \
    IP(dst='255.255.255.255', src='192.168.0.1', id=0)/UDP(dport=80)

wrpcap('input.pcap', pkts)
