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

num_fresh_2 = 0
prev_max = 0
ranges.sort(key=lambda x: x[0])
for r in ranges:
    low = max(r[0], prev_max)
    high = r[1]
    prev_max = max(high + 1, prev_max)
    if high < low:
        continue
    num_fresh_2 += high - low + 1
print(num_fresh_2)
