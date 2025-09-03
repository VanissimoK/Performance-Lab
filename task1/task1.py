import sys
from itertools import cycle

def build_path(n, m):
    lst = list(range(1, n + 1))
    clst = cycle(lst)
    frst = next(clst)
    path = []
    current = frst
    
    while current != frst or len(path) == 0:
        path.append(current)
        for _ in range(m - 1):
            current = next(clst)
    return path

n1, m1, n2, m2 = map(int, sys.argv[1:5])
path1 = build_path(n1, m1)
path2 = build_path(n2, m2)
sumpath = path1 + path2
for i in range(len(sumpath)):
    print(sumpath[i], end='')
