#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#date 2018-09-03

'Change linux hosts template, You need change variables: Hosts_file, S_hosts, s'

__author__ = 'gentleman.zhou@gmail.com'

import shutil
import time
import socket
import re

Hosts_file = '/home/ubuntu/python/hosts'

#Get current time
Current_Time = time.strftime('%Y%m%d%H%I%S',time.localtime(time.time()))

#Get hostname
HostName = socket.gethostname()

#Backup hosts
shutil.copy(Hosts_file, Hosts_file+'.'+Current_Time)

#Edit host to hosts file
S_hosts = ("""127.0.0.1 localhost
127.0.1.1 ubuntu-virtual-machine

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters""")

#Replace string
s = re.sub('127.0.1.1\subuntu-virtual-machine', '127.0.0.1 '+HostName, S_hosts)

#Write hosts
with open(Hosts_file, 'w', encoding='utf-8') as f:
    print(f.write(s))
