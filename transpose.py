#!/usr/bin/env python3
from pprint import pprint as pp

def transpose(*days):
    return list(zip(*days))

if __name__ == '__main__':
    sunday  = [12, 14, 15, 15, 17, 21, 22, 23, 22, 20, 18]
    monday  = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19]
    tuesday = [15, 19, 12, 14, 19, 20, 23, 11, 18, 17, 18]

    days = [sunday, monday, tuesday]

    pp(transpose(*days))
