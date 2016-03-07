#!/usr/bin/env python
# coding:utf-8
#
# changeSSIDall.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-07
#

import sys
import time
from util import *

if __name__ == '__main__':
  if len(sys.argv) != 3 :
    print "Usage: "+sys.argv[0]+" ssid psk"
    sys.exit(1)

  ssid = sys.argv[1]
  psk = sys.argv[2]
  print ssid, psk
  with open(getpath('hosts')) as f :
    for line in f.readlines() :
      line = line.strip()
      if line[0] == "#" : continue # comment
      if line == "" : continue # comment
  
      host = line
      print host, "..."
      print remotecommand(host, ["nvram", "set", "wl0_ssid="+ssid])
      print remotecommand(host, ["nvram", "set", "wl0_akm=psk2"])
      print remotecommand(host, ["nvram", "set", "wl0_security_mode=psk2"])
      print remotecommand(host, ["nvram", "set", "wl0_wpa_psk="+psk])
      print remotecommand(host, ["nvram", "set", "wl0_crypto=tkip"])
      print remotecommand(host, ["nvram", "set", "wl0_wds0=*,auto,tkip,psk2,gateway-testbed,"+psk])
      print remotecommand(host, ["nvram", "set", "wl0_wep=disabled"])
      print remotecommand(host, ["nvram", "set", "wl1_ssid="+ssid])
      print remotecommand(host, ["nvram", "set", "wl1_akm=psk2"])
      print remotecommand(host, ["nvram", "set", "wl1_security_mode=psk2"])
      print remotecommand(host, ["nvram", "set", "wl1_wpa_psk="+psk])
      print remotecommand(host, ["nvram", "set", "wl1_crypto=tkip"])
      print remotecommand(host, ["nvram", "set", "wl1_wds0=*,auto,tkip,psk2,gateway-testbed,"+psk])
      print remotecommand(host, ["nvram", "set", "wl1_wep=disabled"])
      print remotecommand(host, ["nvram", "commit"])
#      remotecommand(host, ["reboot"])

      #remotecommand(host, ["wl", "-i", "eth1", "radio", "off"])
      #remotecommand(host, ["wl", "-i", "eth2", "radio", "off"])
      print remotecommand(host, ["stopservice nas; startservice nas"])
#      print remotecommand(host, ["wl", "-i", "eth1", "radio", "on"])
#      print remotecommand(host, ["wl", "-i", "eth2", "radio", "on"])
      print "\tdone"

