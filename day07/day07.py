#!/usr/bin/env python3
import os

with open(os.path.dirname(os.path.realpath(__file__)) + '/input') as f:
    manifold = [x.strip() for x in f.readlines()]

n = 0
tachyons = {x: 1 for x in [manifold[0].find('S')]}
for i, row in enumerate(manifold[1:]):
    new_tachyons = {}
    for t, nt in tachyons.items():
        if row[t] == '^':
            n += 1
            if t > 0:
                new_tachyons[t-1] = new_tachyons.get(t-1, 0) + nt
            if t < len(row):
                new_tachyons[t+1] = new_tachyons.get(t+1, 0) + nt
        else:
            new_tachyons[t] = new_tachyons.get(t, 0) + nt
    tachyons = new_tachyons

print(n)
print(sum([v for _, v in tachyons.items()]))
