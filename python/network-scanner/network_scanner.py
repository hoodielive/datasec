#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): 
    arp_request = scapy.ARP()
    print(arp_request.summary())
    scapy.ls(scapy.ARP()) 

scan('10.0.1.1/24')
