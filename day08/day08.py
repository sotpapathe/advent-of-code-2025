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
n = 0
for k in list(bloop.keys())[:1000]:
    id1, id2 = bloop[k]
    if id1 in junction_to_circuit and id2 in junction_to_circuit:
        cid1 = junction_to_circuit[id1]
        cid2 = junction_to_circuit[id2]
        if cid1 != cid2:
            merge_circuits(circuit_to_junction, junction_to_circuit, cid1, cid2)
    elif id1 in junction_to_circuit:
        cid = junction_to_circuit[id1]
        junction_to_circuit[id2] = cid
        circuit_to_junction[cid].add(id2)
    elif id2 in junction_to_circuit:
        cid = junction_to_circuit[id2]
        junction_to_circuit[id1] = cid
        circuit_to_junction[cid].add(id1)
    else:
        circuit_to_junction[n] = set([id1, id2])
        junction_to_circuit[id1] = n
        junction_to_circuit[id2] = n
        n += 1

circuit_to_junction = {k: v for k, v in sorted(circuit_to_junction.items(), key=lambda x: len(x[1]))}
largest = list(circuit_to_junction.items())[-3:]
n = math.prod([len(x[1]) for x in largest])
print(n)
