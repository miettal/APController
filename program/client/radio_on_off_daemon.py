#!/usr/bin/env python
# coding:utf-8
#
# radio_on_off_daemon.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-07
#

import traceback
from util import *
import time

if __name__ == '__main__':
  while True :
    try :
      ret = ping("8.8.8.8")
      if ret == 0 :
        print "on"
        command(["wl", "-i", "eth1", "radio", "on"])
        command(["wl", "-i", "eth2", "radio", "on"])
      else :
        print "off"
        command(["wl", "-i", "eth1", "radio", "off"])
        command(["wl", "-i", "eth2", "radio", "off"])
    except :
      print traceback.format_exc()
    time.sleep(10)
