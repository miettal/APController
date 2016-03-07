#!/usr/bin/env python
# coding:utf-8
#
# changeCh.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-07
#

import sys
from util import *

if __name__ == '__main__':
  if len(sys.argv) != 4 :
    print "Usage: "+sys.argv[0]+" host dev ch"
    sys.exit(1)

  host = sys.argv[1]
  dev = sys.argv[2]
  ch = sys.argv[3]
  if dev == "eth1" :
    remotecommand(host, ["nvram", "set", "wl0_channel="+ch])
  elif dev == "eth2" :
    remotecommand(host, ["nvram", "set", "wl1_channel="+ch])
  else :
    print "invlid dev"
    sys.exit(1)
  remotecommand(host, ["nvram", "commit"])
  remotecommand(host, ["stopservice nas; startservice nas"])
