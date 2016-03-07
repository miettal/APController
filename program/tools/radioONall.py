#!/usr/bin/env python
# coding:utf-8
#
# rebootall.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-07
#

import sys
import time
from util import *

if __name__ == '__main__':
  with open(getpath('hosts')) as f :
    for line in f.readlines() :
      line = line.strip()
      if line[0] == "#" : continue # comment
      if line == "" : continue # comment
  
      host = line
      print host + "..."
      remotecommand(host, ["wl", "-i", "eth1", "radio", "on"])
      remotecommand(host, ["wl", "-i", "eth2", "radio", "on"])
      print "\tdone"

