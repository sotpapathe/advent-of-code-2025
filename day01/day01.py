#!/usr/bin/env python3
import os

n = 0
n2 = 0
dial = 50
with open(os.path.dirname(os.path.realpath(__file__)) + '/input3') as f:
    for line in f:
        dir = line[0]
        dist = int(line[1:])
        inc = dist // 100
        n2 += inc
        dist = dist % 100
        at_zero = dial == 0
        if dir == "L":
            dial -= dist
        else:
            dial += dist
        dial_mod = dial % 100
        if dial_mod != dial and not at_zero and dial_mod != 0:
            n2 += 1
        dial = dial_mod
        if dial == 0:
            n += 1
print(n)
print(n + n2)
