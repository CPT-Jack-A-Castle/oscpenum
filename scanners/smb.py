#!/usr/bin/python

from furl import furl
from execute import execute
from pubsub import pubsub


def scan(url: furl):
    # 7.3.2 Nmap SMB NSE Scripts
    execute(f"nmap -v -p 139, 445 --script=smb-os-discovery {url}")
    execute(
        f"nmap -v -p 139,445 --script=smb-vuln-ms08-067 --script-args=unsafe=1 {url}")


pubsub.subscribe("smb", scan)
