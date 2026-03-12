#!/usr/bin/env python3
import os
import math
import numpy as np

def merge_circuits(circuit_to_junction, junction_to_circuit, cid1, cid2):
    for j in circuit_to_junction[cid2]:
        junction_to_circuit[j] = cid1
    circuit_to_junction[cid1] = circuit_to_junction[cid1].union(circuit_to_junction[cid2])
    del circuit_to_junction[cid2]

points = np.genfromtxt(os.path.dirname(os.path.realpath(__file__)) + '/input', delimiter=',', dtype=np.int64)
diff = points[:,None,:] - points[None,:,:]
norms = np.sum(diff**2, axis=-1)

# bloop is a map from a distance to a pair of IDs
bloop = {}
for i in range(norms.shape[0]):
    for j in range(i, norms.shape[1]):
        if i == j:
            continue
        id1 = i if i < j else j
        id2 = j if i < j else i
        dist = norms[i][j]
        assert(dist not in bloop)
        bloop[dist] = (id1, id2)
bloop = {k: v for k, v in sorted(bloop.items(), key=lambda x: x[0])}

junction_to_circuit = {} # int -> int
circuit_to_junction = {} # int -> set[int]
for i in range(norms.shape[0]):
    circuit_to_junction[i] = set([i])
    junction_to_circuit[i] = i
for i, k in enumerate(list(bloop.keys())):
    id1, id2 = bloop[k]
    if id1 in junction_to_circuit and id2 in junction_to_circuit:
        cid1 = junction_to_circuit[id1]
        cid2 = junction_to_circuit[id2]
        if cid1 != cid2:
            merge_circuits(circuit_to_junction, junction_to_circuit, cid1, cid2)
    if i == 999:
        c2j = {k: v for k, v in sorted(circuit_to_junction.items(), key=lambda x: len(x[1]))}
        largest = list(c2j.items())[-3:]
        n = math.prod([len(x[1]) for x in largest])
        print(n)
    if len(circuit_to_junction) == 1:
        x1 = points[id1, 0]
        x2 = points[id2, 0]
        print(x1*x2)
        break
