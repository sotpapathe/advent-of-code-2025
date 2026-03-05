#!/usr/bin/env python3
import os
import numpy as np

points = np.genfromtxt(os.path.dirname(os.path.realpath(__file__)) + '/input_smol', delimiter=',', dtype=np.int64)
diff = points[:,None,:] - points[None,:,:]
norms = np.sum(diff**2, axis=-1)

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

junctions = []
for k in list(bloop.keys())[:10]:
    id1, id2 = bloop[k]
    # TODO: how do we handle the need to connect two junctions?
    for j in junctions:
        if id1 in j or id2 in j:
            j.insert(id1)
            j.insert(id2)
            # TODO: set flag + create new junction with id1,id2 if unset?

print(junctions)
