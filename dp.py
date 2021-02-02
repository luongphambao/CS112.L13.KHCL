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
    path = [1]
    while (end, s) in p:
        item = p[end, s]
        s = item[1]
        end = item[0]
        path.insert(0, end)
    path.insert(0, 1)
    return path, minCost


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
    minCost = get_minimum1(C, end, s, g)
    if minCost == infinity:
        return []
    return minCost
def get_minimum1(C, v, S, g):
    if (v, S) in g:
        return g[v, S]

    values = []
    all_min = []
    for j in S:
        set_a = copy.deepcopy(list(S))
        set_a.remove(j)
        if C[v-1][j-1]!=infinity:
          all_min.append([j, tuple(set_a)])
          result = get_minimum1(C, j, tuple(set_a), g)
          values.append(C[v-1][j-1] + result)
    if len(values)==0:
      g[v,S]=infinity
    else:
      g[v, S] = min(values)
    return g[v, S]
