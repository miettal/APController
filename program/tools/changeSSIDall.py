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
      remotecommand(host, ["nvram", "set", "wl0_ssid="+ssid])
      remotecommand(host, ["nvram", "set", "wl0_akm=psk2"])
      remotecommand(host, ["nvram", "set", "wl0_auth_mode=none"])
      remotecommand(host, ["nvram", "set", "wl0_authmode=open"])
      remotecommand(host, ["nvram", "set", "wl0_security_mode=psk2"])
      remotecommand(host, ["nvram", "set", "wl0_wpa_psk="+psk])
      remotecommand(host, ["nvram", "set", "wl0_crypto=aes"])
      remotecommand(host, ["nvram", "set", "wl0_wds0=*,auto,aes,psk2,gateway-testbed,"+psk])
      remotecommand(host, ["nvram", "set", "wl0_wep=disabled"])

      remotecommand(host, ["nvram", "set", "wl1_ssid="+ssid])
      remotecommand(host, ["nvram", "set", "wl1_akm=psk2"])
      remotecommand(host, ["nvram", "set", "wl1_auth_mode=none"])
      remotecommand(host, ["nvram", "set", "wl1_authmode=open"])
      remotecommand(host, ["nvram", "set", "wl1_security_mode=psk2"])
      remotecommand(host, ["nvram", "set", "wl1_wpa_psk="+psk])
      remotecommand(host, ["nvram", "set", "wl1_crypto=aes"])
      remotecommand(host, ["nvram", "set", "wl1_wds0=*,auto,aes,psk2,gateway-testbed,"+psk])
      remotecommand(host, ["nvram", "set", "wl1_wep=disabled"])
      remotecommand(host, ["nvram", "commit"])
      remotecommand(host, ["stopservice nas; startservice nas"])
      print "\tdone"

