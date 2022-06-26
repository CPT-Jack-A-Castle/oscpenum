#!/usr/bin/python

from furl import furl
from execute import execute, cache
from pubsub import pubsub

import socket


@cache.memoize()
def scan(url: furl):
    # 7.5 SMTP Enumeration
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url.host, url.port))
    banner = s.recv(1024)
    print(banner.decode())
    s.send(b"VRFY ROOT\r\n")
    result = s.recv(1024)
    print(result.decode())
    s.close()


pubsub.subscribe("smtp", scan)
