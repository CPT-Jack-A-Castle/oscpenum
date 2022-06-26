#!/usr/bin/python

from sortedcontainers import SortedSet
import re
from execute import execute
from pubsub import pubsub
from furl import furl
from scanners import *


def scrape_nmap_services(output: str) -> SortedSet:
    exp = r"(\d+)\/(\w+)\W+open\W+(\w+)"
    return SortedSet(re.findall(exp, output, flags=re.MULTILINE))


def scape_masscan_ports(output: str) -> SortedSet:
    exp = r"Discovered open port (\d*)/(\w*) on .*"
    return SortedSet(re.findall(exp, output, flags=re.MULTILINE))


def ports(addr: str):
    # execute(f"nmap -Pn {addr}")
    # execute(f"nmap -Pn -p 1-65535 {addr}")
    # 7.2.2.2 Stealth / SYN Scanning
    # execute(f"nmap -Pn -sS {addr}")

    # 7.2.2.3 TCP Connect Scanning
    # execute(f"nmap -Pn -sT {addr}")

    # 7.2.2.4 UDP Scanning
    # execute(f"nmap -Pn -sU {addr}")
    # execute(f"nmap -Pn -sS -sU {addr}")

    nmap_services = scrape_nmap_services(
        execute(f"nmap -Pn -sC -sV -sT {addr}"))
    for port, _, scheme in nmap_services:
        url = furl(f"{scheme}://{addr}:{port}")
        pubsub.publish(url)

    # 7.2.2.6 OS Fingerprinting
    # execute(f"nmap -Pn -O {addr}")

    # 7.2.3 Masscan
    masscan_services = scape_masscan_ports(
        execute(f"sudo masscan {addr} --ports 0-65535 --rate=10000"))
    masscan_services = masscan_services.difference(nmap_services)
    for port, _, scheme in masscan_services:
        url = furl(f"{scheme}://{addr}:{port}")
        pubsub.publish(url)

    # 8.3 Vulnerability Scanning with Nmap
    execute(f"nmap -O --script vuln {addr}")


def main():
    addr = "10.10.11.166"
    # addr = "127.0.0.1"
    ports(addr)


if __name__ == "__main__":
    main()
