#!/usr/bin/python

from furl import furl
from execute import execute
from pubsub import pubsub


def scan(url: furl):
    # 7.6.2 Scanning for SNMP
    execute(f"nmap -sU --open -p 161 {url.host}")
    execute(
        f"onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings-onesixtyone.txt -i {url.host}")

    # 7.6.3.1 Enumerating the Entire MIB Tree
    execute(f"snmpwalk -c public -v1 -t 10 {url.host}")

    # 7.6.3.2 Enumerating Windows Users
    execute(f"snmpwalk -c public -v1 {url.host} 1.3.6.1.4.1.77.1.2.25")

    # 7.6.3.3 Enumerating Running Windows Processes
    execute(f"snmpwalk -c public -v1 {url.host} 1.3.6.1.2.1.25.4.2.1.2")

    # 7.6.3.4 Enumerating Open TCP Ports
    execute(f"snmpwalk -c public -v1 {url.host} 1.3.6.1.2.1.6.13.1.3")

    # 7.6.3.5 Enumerating Installed Software
    execute(f"snmpwalk -c public -v1 {url.host} 1.3.6.1.2.1.25.6.3.1.2")


pubsub.subscribe("snmp", scan)
