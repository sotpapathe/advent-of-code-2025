#!/usr/bin/env python3
import functools
import os
import tqdm

# TODO: use Point class, find why the number of intersections is wrong

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def rect_coords(p1, p2):
    return [p1, p2, (p1[0], p2[1]), (p2[0], p1[1])]


# l*: List[Tuple, Tuple]
def lines_intersect(l1, l2):
    # l1 (ray) is always horizontal
    # l1[0] (ray start) is always outside the polygon
    # l1[1] (ray end) is always the query point
    qx = l1[1][0]
    qy = l1[1][1]
    l2_hor = l2[0][1] == l2[1][1]
    if l2_hor:
        if l2[0][1] == l1[0][1]:
            # colinear
            return l2[0][0] <= qx and qx <= l2[1][0]
        else:
            # parallel, no intersection
            return False
    else:
        # perpendicular
        l1y = l1[0][1]
        l2x = l2[0][0]
        return l1[0][0] <= l2x and l2x <= l1[1][0] \
                and l2[0][1] <= l1y and l1y <= l2[1][1]



def point_in_poly(p, poly, rayx):
    ray = [(rayx, p[1]), p]
    n_intersections = 0
    for i in range(len(poly)):
        if lines_intersect(ray, [poly[i], poly[(i + 1) % len(poly)]]):
            n_intersections += 1
    print(p, n_intersections)
    return n_intersections % 2 == 1


coords = []
with open(os.path.dirname(os.path.realpath(__file__)) + '/input_smol') as f:
    for line in f:
        coords.append([int(x) for x in line.split(',')])

rayx = min([x[0] for x in coords]) - 1

max_area = 0
for i in tqdm.tqdm(range(len(coords))):
    for j in range(i + 1, len(coords)):
        c = rect_coords(coords[i], coords[j])
        inside = [point_in_poly(x, coords, rayx) for x in c]
        inside2 = functools.reduce(lambda x, y: x and y, inside)
        a = area(coords[i], coords[j])
        if coords[i][0] == 9 and coords[i][1] == 5 \
                and coords[j][0] == 2 and coords[j][1] == 3:
            print(c)
            print(a)
            print(inside)
        if inside2 and a > max_area:
            max_area = a
            #print(coords[i], coords[j])

print(max_area)

#..............
#.......#XXX#..
#.......X...X..
#..#XXXX#...X..
#..X........X..
#..#XXXXXX#.X..
#.........X.X..
#.........#X#..
#..............

#..............
#.......#XXX#..
#.......X...X..
#..#XXXX#...X..
#--X-->.....X..
#..#XXXXXX#.X..
#----->...X.X..
#.........#X#..
#..............
