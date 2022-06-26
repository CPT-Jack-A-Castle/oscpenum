#!/usr/bin/python

from furl import furl
from execute import execute
from pubsub import pubsub


def scan(url: furl):
    # 7.3.1 Scanning for the NetBIOS Service
    execute(f"sudo nbtscan -r {url}")
    execute(f"nmap -v -p 139, 445 --script=smb-os-discovery {url}")


pubsub.subscribe("netbios", scan)
