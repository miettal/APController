#!/usr/bin/env python
# coding:utf-8
#
# deploy.py
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

      print host+"...",

#      remotecommand(host, ["rm", "-rf", "/jffs/APController"])
#      remotecommand(host, ["mkdir", "-p", "/jffs/APController"])

      remotedst = "/jffs/APController/"

      localsrc = getpath("/program")
      copy(host, localsrc, remotedst)
      localsrc = getpath("/hosts")
      copy(host, localsrc, remotedst)
      localsrc = getpath("/openwrt/build_dir/target-arm_cortex-a9_musl-1.1.14_eabi/root-bcm53xx/lib/ld-musl-arm.so.1")
      copy(host, localsrc, remotedst)
#      localsrc = getpath("/python/Python-2.7.1_build")
#      copy(host, localsrc, remotedst)

      rc_startup = open(getpath("/program/misc/rc_startup")).read()
      remotecommand(host, ["nvram", "set", "rc_startup=\""+rc_startup+"\""])
      remotecommand(host, ["nvram", "commit"])

      print "done"
