#!/usr/bin/env python3
import os

def accessible(rolls, x, y):
    if not rolls[y][x]:
        return False
    n = 0
    for yy in [-1, 0, 1]:
        for xx in [-1, 0, 1]:
            if xx == 0 and yy == 0:
                continue
            if x + xx < 0 or x + xx >= len(rolls[0]) or y + yy < 0 or y + yy >= len(rolls):
                continue
            if rolls[y + yy][x + xx]:
                n += 1
    return n < 4


with open(os.path.dirname(os.path.realpath(__file__)) + '/input') as f:
    rolls = [x.strip() for x in f.readlines()]
rolls = [[True if col == '@' else False for col in row] for row in rolls]

n_rolls = 0
update = True
while update:
    update = False
    removed = []
    for y in range(len(rolls)):
        for x in range(len(rolls[y])):
            if accessible(rolls, x, y):
                n_rolls += 1
                removed.append((x, y))
                update = True
    for r in removed:
        rolls[r[1]][r[0]] = False

print(n_rolls)
