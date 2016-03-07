#!/usr/bin/env python
# coding:utf-8
#
# showhosts.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-06
#
from util import *

if __name__ == '__main__':
  with open(getpath('hosts')) as f :
    for line in f.readlines() :
      line = line.strip()
      if line[0] == "#" : continue # comment
      if line == "" : continue # comment
  
      host = line
      try :
        print host,
        print "\t\t\t hostname:{:s}".format(gethostinfo(host)),
        print "\t\t ping(localhost->AP):{:s}".format("OK" if ping(host) == 0 else "NG"),
        print "\t ping(AP -> 8.8.8.8):{:s}".format("OK" if ping2(host, "8.8.8.8") == 0 else "NG")

        print "\t eth1(wl0, 5.0GHz)...",
        print "\t radio:{:3s}".format("on" if remotecommand(host, ["wl","-i","eth1","radio"])[0].strip() == "0x0000" else "off"),
        print "\t\t SSID:{:16s}".format(remotecommand(host, ["wl","-i","eth1","ssid"])[0].split()[-1][1:-1]),
        print "\t\t PSK:{:16s}".format(remotecommand(host, ["nvram", "get", "wl0_wpa_psk"])[0][:-1]),
        print "\t\t Ch:{:3s}".format(remotecommand(host, ["nvram", "get", "wl0_channel"])[0][:-1]),
        print "\t TXPWR:{:4s}".format(''.join(remotecommand(host, ["wl", "-i", "eth1", "txpwr1"])[0].split()[6:7])),
        print "\t assoc num:{:2d}".format(
            len([ mac for mac in remotecommand(host, ["wl", "-i", "eth1", "assoclist"])[0].split('\n') if mac.strip() != ""]))

        print "\t eth2(wl1, 2.4GHz)...",
        print "\t radio:{:3s}".format("on" if remotecommand(host, ["wl","-i","eth2","radio"])[0].strip() == "0x0000" else "off"),
        print "\t\t SSID:{:16s}".format(remotecommand(host, ["wl","-i","eth2","ssid"])[0].split()[-1][1:-1]),
        print "\t\t PSK:{:16s}".format(remotecommand(host, ["nvram", "get", "wl1_wpa_psk"])[0][:-1]),
        print "\t\t Ch:{:3s}".format(remotecommand(host, ["nvram", "get", "wl1_channel"])[0][:-1]),
        print "\t TXPWR:{:4s}".format(''.join(remotecommand(host, ["wl", "-i", "eth2", "txpwr1"])[0].split()[6:7])),
        print "\t assoc num:{:2d}".format(
            len([ mac for mac in remotecommand(host, ["wl", "-i", "eth2", "assoclist"])[0].split('\n') if mac.strip() != ""]))

      except:
        print "failed"
        continue
