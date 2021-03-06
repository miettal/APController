#!/usr/bin/env python
# coding:utf-8
#
# util.py
#
# Author:   Hiromasa Ihara (taisyo)
# Created:  2016-03-06
#
import os
from subprocess import *

def getpath(path) :
  if path[0] == "/" : path = path[1:]
  d = os.path.dirname(__file__)
  p = os.path.join(d, '../../', path)
  return p

def command(cmd, inpt="") :
  if type(cmd) is not list: cmd = [cmd]
  p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
  out, err = p.communicate(inpt)
  ret = p.wait()
  return out, err, ret

def isradioon(dev) :
  return 1 if command(["wl","-i",dev,"radio"])[0].strip() == "0x0000" else 0

def remotecommand(host, cmd, inpt="") :
  if type(cmd) is not list: cmd = [cmd]
  return command(["ssh", "-o", "ConnectTimeout=2", "root@"+host] + cmd)

def gethostinfo(host) :
  out, err, ret = remotecommand(host, "hostname")
  return out[:-1]

def ping(host) :
  out, err, ret = command(["ping", "-c", "1", "-W", "1", host])
  return ret

def copy(host, localsrc, remotedst) :
  out, err, ret = command(["scp", "-r", localsrc, "root@"+host+":"+remotedst])
