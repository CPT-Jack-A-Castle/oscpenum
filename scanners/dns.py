#!/usr/bin/python

from furl import furl
from execute import execute
from pubsub import pubsub


def scan(url: furl):
    # 7.1.1 Interacting with a DNS Server
    execute(f"host {url.host}")
    execute(f"host -t mx {url.host}")
    execute(f"host -t txt {url.host}")

    # 7.1.6.1 DNSRecon
    execute(f"dnsrecon -d {url.host} -t axfr")

    # 7.1.6.2 DNSenum
    execute(f"dnsenum {url.host}")


pubsub.subscribe("domain", scan)
