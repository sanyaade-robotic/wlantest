#!/usr/bin/python
##
## wlantest.py
##
## Script for automatic wireless testing using hostapd
##
## Author(s):
##  - Maxence VIALLON <mviallon@aldebaran-robotics.com>
##

import os

from ConnmanClient import ConnmanClient
from Hostapd import Hostapd

class wlantest:

    def __init__(self):
        self.connman = ConnmanClient()
        self.hostapd = Hostapd()

    def open(self, ssid):
        self.hostapd.open(ssid)
        print("Hostap running mode open")

        self.testpsk(ssid, None)
    
    def wpa2(self, ssid, passphrase):
        self.hostapd.wpa2(ssid, passphrase)
        print("Hostap running mode wpa2")

        self.testpsk(ssid, passphrase)
        
    def wpa(self, ssid, passphrase):
        self.hostapd.wpa(ssid, passphrase)
        print("Hostap running mode wpa")

        self.testpsk(ssid, passphrase)

    def testpsk(self, ssid, passphrase):

        print("Scanning wifi ...")
        self.connman.scan()

        print("Connecting to network ...")
        ServiceId = self.connman.getServiceId(ssid)

        self.connman.setPassphrase(passphrase)
        self.connman.connect(ServiceId)
    
        print("Checking network status ...")
        if self.connman.serviceisConnected(ServiceId):
            print "Success !"
        else:
            print "Fail"

        print("Disconnecting ...")
        self.connman.disconnect(ServiceId)

    def stop(self):
        self.hostapd.kill()

if (__name__ == "__main__"):
    
    # TODO : Start dhcp

    wlantest = wlantest()
    
    wlantest.open("openrezo")

    wlantest.wpa2("wpa2rezo", "12345678")

    wlantest.wpa("wparezo", "42424242")

    wlantest.stop()
    
