#!/usr/bin/env python
# coding:utf-8
#
# changePower.py
#
# Author:   Hiromasa Ihara (miettal)
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
  _, err, ret = remotecommand(host, ["wl", "-i", dev, "txpwr", str(power)])
