#!/usr/bin/python

from furl import furl
from execute import execute, cache
from pubsub import pubsub
import requests


@cache.memoize()
def robots(url: furl):
    # 9.2.4 Inspecting Sitemaps
    return requests.get(url / "robots.txt")


def dirb(url: furl):
    # 9.3.2 DIRB
    execute(f"dirb {url} -r -z 10")


def nikto(url: furl):
    # 9.3.4 Nikto
    execute(f"nikto -host={url} -maxtime=30s")


def scan(url: furl):
    response = requests.head(url)
    print(response.content)
    print(response.headers)

    r = robots(url)
    if r.status_code != 404:
        print(r.content)

    dirb(url)
    nikto(url)


# https://github.com/hakluke/hakrawler
# wpscan --url sandbox.local --enumerate ap,at,cb,dbe

pubsub.subscribe("http", scan)
