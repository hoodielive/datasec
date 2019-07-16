#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): 
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether()
    scapy.ls(broadcast)

scan('10.0.1.1/24')
