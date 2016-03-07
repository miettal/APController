#!/usr/bin/env python
# coding:utf-8
#
# gen_syslog_daemon.py
#
# Author:   Hiromasa Ihara (miettal)
# URL:      http://miettal.com
# License:  MIT License
# Created:  2016-03-08
#

import time
from util import *

if __name__ == '__main__':
  assoclist_eth1 = [ mac for mac in command(["wl", "-i", "eth1", "assoclist"])[0].split('\n') if mac.strip() != ""]
  assoclist_eth2 = [ mac for mac in command(["wl", "-i", "eth2", "assoclist"])[0].split('\n') if mac.strip() != ""]
  
  while True :
    new_assoclist_eth1 = [ mac for mac in command(["wl", "-i", "eth1", "assoclist"])[0].split('\n') if mac.strip() != ""]
    new_assoclist_eth2 = [ mac for mac in command(["wl", "-i", "eth2", "assoclist"])[0].split('\n') if mac.strip() != ""]

    print "disassoc eth1(5GHz)"
    for disassoc_mac in set(assoclist_eth1) - set(new_assoclist_eth1) :
      print disassoc_mac
    print

    print "disassoc eth2(2.4GHz)"
    for disassoc_mac in set(assoclist_eth2) - set(new_assoclist_eth2) :
      print disassoc_mac
    print

    print "assoc eth1(5GHz)"
    for assoc_mac in set(new_assoclist_eth1) - set(assoclist_eth1) :
      print assoc_mac
    print

    print "assoc eth2(2.4GHz)"
    for assoc_mac in set(new_assoclist_eth2) - set(assoclist_eth2) :
      print assoc_mac
    print

    assoclist_eth1 = new_assoclist_eth1
    assoclist_eth2 = new_assoclist_eth2

    time.sleep(1)
