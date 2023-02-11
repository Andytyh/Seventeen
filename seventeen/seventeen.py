from math import log10, floor


def a(n):
    if n == 0:
        return 17
    else:
        return n*10**(floor(log10(a(n-1))+3)) + 17*10**(floor(log10(a(n-1))+1)) + a(n-1) # noqa
