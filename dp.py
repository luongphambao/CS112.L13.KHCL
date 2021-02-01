import sys
import copy
import random
import cProfile
import time
from random import seed
from random import randint
import copy
infinity = float('inf')
def dynamic(matrix):
    g = {}
    p = {}
    n = len(matrix)
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]
        v = [i+2 for i in range(n-1)]
        s = tuple(v)
    end = 1
    minCost = get_minimum(matrix, end, s, g, p)
    infinity = float('inf')
    if minCost == infinity:
        return []
    return minCost
def get_minimum(C, v, S, g, p):
    if (v, S) in g:
        return g[v, S]
    values = []
    all_min = []
    for j in S:
        set_a = copy.deepcopy(list(S))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(C, j, tuple(set_a), g, p)
        values.append(C[v-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[v, S] = min(values)
    p[v, S] = all_min[values.index(g[v, S])]

    return g[v, S]
def dynamic1(C):
    g = {}
    n = len(C)
    for x in range(1, n):
        g[x + 1, ()] = C[x][0]
        v = [i+2 for i in range(n-1)]
        s = tuple(v)
    end = 1
    minCost = get_minimum(C, end, s, g)
    if minCost == infinity:
        return []
    return minCost
def get_minimum1(C, v, S, g):
    if (v, S) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[v, S]

    values = []
    all_min = []
    for j in S:
        set_a = copy.deepcopy(list(S))
        set_a.remove(j)
        if C[v-1][j-1]!=infinity:
          all_min.append([j, tuple(set_a)])
          result = get_minimum(C, j, tuple(set_a), g)
          values.append(C[v-1][j-1] + result)


    # get minimun value from set as optimal solution for
    if len(values)==0:
      g[v,S]=infinity
    else:
      g[v, S] = min(values)
    return g[v, S]
C = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
minCost = dynamic(C)

print('Do dai:', minCost)