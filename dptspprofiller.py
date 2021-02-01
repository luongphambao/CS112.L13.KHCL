
import sys
import copy
import random
import cProfile
import time
from random import seed
from random import randint
import copy

def generate_input(n,k):
  data=[]
  for i in range(0,k):
    n=int(n)
    graph_generate=generate(n)
    data.append(graph_generate)
    
  return data

def generate(n):
  arr=[]
  arr1=[]
  for i in range(0,n):
    for j in range(0,n):
        if i==j:
          arr1.append(0)
        else:
          arr1.append(randint(1,1000))
    arr.append(arr1)
    arr1=[]
  return arr




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

C = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]


minCost = dynamic(C)

print('Do dai:', minCost)

for s in range(4,12):
    getData=generate_input(s,1)
    for i in range(len(getData)):
              C=getData[i]
              n=int(s)
              v = [False for j in range(n)] 
              v[0] = True
              answer=[]
              matrix=C
              cProfile.run(f'dynamic({matrix})')