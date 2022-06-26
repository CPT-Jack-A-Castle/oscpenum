#!/usr/bin/python

from subprocess import run, CompletedProcess
from diskcache import Cache

cache = Cache(".")


@cache.memoize()
def cache_execute(cmd: str) -> CompletedProcess:
    return run(cmd.split(), capture_output=True)


def execute(cmd: str):
    cp = cache_execute(cmd)
    print(cp.stdout.decode())
    return cp.stdout.decode()
