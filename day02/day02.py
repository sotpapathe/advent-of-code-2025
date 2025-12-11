#!/usr/bin/env python3
# (+){2,}
import os

class Range:
    def __init__(self, range):
        r = range.split('-')
        self.start = int(r[0])
        self.end = int(r[1])

    def __str__(self) -> str:
        return '{}-{}'.format(self.start, self.end)

n = 0
n2 = 0
with open(os.path.dirname(os.path.realpath(__file__)) + '/input') as f:
    ranges = [Range(x) for x in f.readlines()[0].strip().split(',')]
    for r in ranges:
        for x in range(r.start, r.end + 1):
            s = str(x)
            # Part 1
            if len(s) % 2 == 0:
                if s[:len(s)//2] == s[len(s)//2:]:
                    n += x
            # Part 2
            for seqlen in range(1, len(s)//2 + 1):
                if len(s) % seqlen != 0:
                    continue
                seq = s[:seqlen]
                r = len(s) // seqlen
                if s == r * seq:
                    n2 += x
                    break

print(n)
print(n2)
