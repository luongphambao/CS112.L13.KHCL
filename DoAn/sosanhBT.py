import sys
import random
import cProfile
import time
from random import seed
from random import randint
from generateInput2 import createArray2D
from generateInput2 import generateInputGraph
from backtracking import tspbacktrack
from backtracking import tspbacktrack1
from lietke import tsplietke
from backtracking import findPath
from backtracking import findPath1
import sys
from numpy import inf
n=7
C=createArray2D(n)
s=n*(n-1)
l=25
countEdge=0
print(f'so thanh pho: {n}')
print(f'so canh: {l}')
C=generateInputGraph(n,C,l,countEdge)
v = [False for i in range(n)]
v[0] = True
currPos,count,cost=0,1,0

cProfile.run(f'tspbacktrack({C}, {currPos},{v}, {n}, {count}, {cost},{[]},{[]})')
v = [False for i in range(n)]
v[0] = True
currPos,count,cost=0,1,0
cProfile.run(f'tspbacktrack1({C}, {currPos},{v}, {n}, {count}, {cost},{[]},{[]})')
