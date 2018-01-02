"""
Important metadata from base function can get lost when decorating
e.g. `__name__` & `__doc__`

Use `functools.wraps()` to properly update metdata
"""

import functools

def noop(fn):
    @functools.wraps(fn)
    def noop_wrap():
        return fn()
    return noop_wrap


def hello():
    "Print a well known message."
    print('Hello, world!')
