#!/usr/bin/env python
# coding:utf-8
#
# changePower.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-07
#
import sys
from util import *

if __name__ == '__main__':
  if len(sys.argv) != 4 :
    print "Usage: "+sys.argv[0]+" host dev power[mW]"
    sys.exit(1)
  
  host = sys.argv[1]
  dev = sys.argv[2]
  power = int(sys.argv[3])
  if not (0 <= power <= 1000) :
    print "available power... 0-1000mW",
    sys.exit(1)

  if dev == "eth1" :
    remotecommand(host, ["nvram", "set", "wl0_txpwr="+str(power)])
    remotecommand(host, ["nvram", "set", "wl0_txpwrusr=0"])
  elif dev == "eth2" :
    remotecommand(host, ["nvram", "set", "wl1_txpwr="+str(power)])
    remotecommand(host, ["nvram", "set", "wl1_txpwrusr=0"])
  else :
    print "invlid dev"
    sys.exit(1)
  remotecommand(host, ["nvram", "commit"])
  remotecommand(host, ["stopservice nas; startservice nas"])
