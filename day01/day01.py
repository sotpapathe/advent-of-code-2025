#!/usr/bin/env python3
import os

n = 0
dial = 50
with open(os.path.dirname(os.path.realpath(__file__)) + '/input') as f:
    for line in f:
        dir = line[0]
        dist = int(line[1:])
        if dir == "L":
            dial -= dist
        else:
            dial += dist
        dial = dial % 100
        if dial == 0:
            n += 1
print(n)
