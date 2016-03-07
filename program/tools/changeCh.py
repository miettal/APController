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
  _, err, ret = remotecommand(host, ["wl", "-i", dev, "channel", ch])
  if ret != 0 :
    print err
    print "available channels...",
    out, _, _ = remotecommand(host, ["wl", "-i", dev, "channels"])
    print out
