#!/usr/bin/python

from furl import furl
from execute import execute
from pubsub import pubsub


def scan(url: furl):
    # 7.4.1 Scanning for NFS Shares
    execute(f"nmap -v -p {url.port} {url.host}")
    execute(f"nmap -sV -p {url.port} --script=rpcinfo {url.host}")

    # 7.4.2 Nmap NFS NSE Scripts
    execute(f"nmap -p 111 --script nfs* {url.host}")
    # sudo mount -o nolock 10.11.1.72:/home ~/home/


pubsub.subscribe("nfs", scan)
