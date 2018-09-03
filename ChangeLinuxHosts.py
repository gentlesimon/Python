#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#date 2018-09-03

'Change linux hosts template'

__author__ = 'gentleman.zhou@gmail.com'

import shutil
import time
import socket
import re


#Get current time
Current_Time = time.strftime('%Y%m%d%H%I%S',time.localtime(time.time()))
#Get hostname
HostName = socket.gethostname()

#Backup hosts
shutil.copy("/home/ubuntu/python/hosts", "/home/ubuntu/python/host."+Current_Time)

#Edit hosts file
with open('/home/ubuntu/python/hosts', 'w', encoding='utf-8') as f:
    print(f.write("""127.0.0.1 localhost
127.0.1.1 ubuntu-virtual-machine

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters"""))

#Replace string
with open('/home/ubuntu/python/hosts', 'r', encoding='utf-8') as f_replace:
    s = f_replace.read()
a = re.sub('127.0.1.1\subuntu-virtual-machine', '127.0.0.1 '+HostName, s)

with open('/home/ubuntu/python/hosts', 'w', encoding='utf-8') as f:
    print(f.write(a))
