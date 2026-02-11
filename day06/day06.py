#!/usr/bin/env python3
import math
import numpy as np
import os

filename = os.path.dirname(os.path.realpath(__file__)) + '/input'

d = np.genfromtxt(filename, dtype=str)
numbers = d[:-1,:].astype(int)
operators = d[-1,:]

results = []
for i in range(numbers.shape[1]):
    if operators[i] == '+':
        results.append(int(numbers[:,i].sum()))
    else:
        results.append(int(numbers[:,i].prod()))
print(sum(results))



with open(filename) as f:
    d = f.readlines()
d = [x.rstrip('\n') for x in d]
numbers = d[:-1]
operators = d[-1]

op_idx = []
for i, c in enumerate(operators):
    if c != ' ':
        op_idx.append(i)
op_idx.append(len(operators) + 1)

results2 = []
for i, start in enumerate(op_idx[:-1]):
    end = op_idx[i + 1] - 1
    n = []
    for row in numbers:
        n.append(row[start:end])
    nums = []
    for j in range(len(n[0])):
        nums.append(int(''.join([x[j] for x in n if x[j] != ' '])))
    if operators[start] == '+':
        results2.append(sum(nums))
    else:
        results2.append(math.prod(nums))
print(sum(results2))
