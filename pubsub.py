#!/usr/bin/python

from furl import furl
from collections import defaultdict
from colorama import Fore, Back, Style


def found(url: furl):
    return Fore.GREEN + f"[*] Found {url}" + Style.RESET_ALL


def no_subscribers(scheme: str):
    return Fore.RED + f"[*] No subscribers for {scheme}" + Style.RESET_ALL


class PubSub:
    def __init__(self):
        self._subscribers = defaultdict(set)
        self._found = set()

    def publish(self, url: furl) -> None:
        if hash(str(url)) not in self._found:
            self._found.add(hash(str(url)))
            print(found(url))

            if url.scheme in self._subscribers:
                for c in self._subscribers[url.scheme]:
                    c(url)
            else:
                print(no_subscribers(url.scheme))

    def subscribe(self, scheme: str, callable) -> None:
        self._subscribers[scheme].add(callable)


pubsub = PubSub()
