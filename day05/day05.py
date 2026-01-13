#!/usr/bin/env python3
import os

ranges = []
ingredients = []
in_ranges = True
with open(os.path.dirname(os.path.realpath(__file__)) + '/input') as f:
    for line in f:
        line = line.strip()
        if line == '':
            in_ranges = False
            continue
        if in_ranges:
            ranges.append([int(x) for x in line.split('-')])
        else:
            ingredients.append(int(line))

num_fresh = 0
for i in ingredients:
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            num_fresh += 1
            break
print(num_fresh)

# TODO: part 2: set OOM
