import sys


def make_set(elem):
    Parent[elem] = elem
    Sz[elem] = 1

def find(elem):
    while Parent[elem] is not elem:
        Parent[elem] = Parent[Parent[elem]]
        elem = Parent[elem]
    return elem


def union(elem1, elem2):
    print(elem1 + " "  + elem2)
    root1, root2 = find(elem1), find(elem2)
    if root1 is not root2:
        if Sz[root1] < Sz[root2]:
            root1, root2 = root2, root1
        Parent[root2] = root1
        Sz[root1] += Sz[root2]

Parent, Sz = {}, {}


infile = sys.stdin
next(infile)

for line in infile:
    make_set(line[0])
    make_set(line[1])
    union(line[0], line[1])

for lin in sys.stdin:
    size = lin[0]
    break
