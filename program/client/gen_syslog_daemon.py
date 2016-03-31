#!/usr/bin/env python
# coding:utf-8
#
# gen_syslog_daemon.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-08
#

import syslog
import time
from util import *

if __name__ == '__main__':
  syslog.openlog('WirelessAP', syslog.LOG_DAEMON|syslog.LOG_PERROR,syslog.LOG_SYSLOG)

  assoclist_eth1 = [ mac for mac in command(["wl", "-i", "eth1", "assoclist"])[0].split('\n') if mac.strip() != ""]
  assoclist_eth2 = [ mac for mac in command(["wl", "-i", "eth2", "assoclist"])[0].split('\n') if mac.strip() != ""]

  radio_state_eth1 = isradioon("eth1")
  radio_state_eth2 = isradioon("eth2")
  
  while True :
    new_assoclist_eth1 = [ mac for mac in command(["wl", "-i", "eth1", "assoclist"])[0].split('\n') if mac.strip() != ""]
    new_assoclist_eth2 = [ mac for mac in command(["wl", "-i", "eth2", "assoclist"])[0].split('\n') if mac.strip() != ""]
    new_radio_state_eth1 = isradioon("eth1")
    new_radio_state_eth2 = isradioon("eth2")

    for assoc_mac in set(new_assoclist_eth1) - set(assoclist_eth1) :
      syslog.syslog(syslog.LOG_NOTICE, 'assoc eth1(wl0,5GHz) mac:{:s}'.format(assoc_mac))

    for assoc_mac in set(new_assoclist_eth2) - set(assoclist_eth2) :
      syslog.syslog(syslog.LOG_NOTICE, 'assoc eth2(wl1,2.4GHz) mac:{:s}'.format(assoc_mac))

    for disassoc_mac in set(assoclist_eth1) - set(new_assoclist_eth1) :
      syslog.syslog(syslog.LOG_NOTICE, 'disassoc eth1(wl0,5GHz) mac:{:s}'.format(disassoc_mac))

    for disassoc_mac in set(assoclist_eth2) - set(new_assoclist_eth2) :
      syslog.syslog(syslog.LOG_NOTICE, 'disassoc eth2(wl1,2.4GHz) mac:{:s}'.format(disassoc_mac))

    if radio_state_eth1 != new_radio_state_eth1 :
      if new_radio_state_eth1 == 1:
        syslog.syslog(syslog.LOG_NOTICE, 'radio eth1(wl0,5GHz) on')
      else :
        syslog.syslog(syslog.LOG_NOTICE, 'radio eth1(wl0,5GHz) off')

    if radio_state_eth2 != new_radio_state_eth2 :
      if new_radio_state_eth2 == 1:
        syslog.syslog(syslog.LOG_NOTICE, 'radio eth2(wl1,2.4GHz) on')
      else :
        syslog.syslog(syslog.LOG_NOTICE, 'radio eth2(wl1,2.4GHz) off')

    assoclist_eth1 = new_assoclist_eth1
    assoclist_eth2 = new_assoclist_eth2
    radio_state_eth1 = new_radio_state_eth1
    radio_state_eth2 = new_radio_state_eth2

    time.sleep(1)
