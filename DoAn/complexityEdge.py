import random
import cProfile
import time
from random import seed
from random import randint
from generateInput2 import createArray2D
from generateInput2 import generateInputGraph
from backtracking import tspbacktrack1
from dp import dynamic 
from dp import dynamic1
from backtracking import findPath1
import sys
from numpy import inf
#CODE ẢNH HƯỞNG CỦA CẠNH LÊN BACKTRACKING
n=7
C=createArray2D(n)
s=n*(n-1)
l=25
countEdge=0
print(f'so canh: {l}')
C=generateInputGraph(n,C,l,countEdge)
v = [False for i in range(n)] 
v[0] = True
currPos,count,cost=0,1,0
print(C)

cProfile.run(f'tspbacktrack1({C}, {currPos},{v}, {n}, {count}, {cost},{[]},{[]})')
print(findPath1(C))
for i in range(l+1,s+1):
  print(f'so canh: {i}')
  C=generateInputGraph(n,C,i,i-1)#tăng so canh len 1
  v = [False for i in range(n)] 
  v[0] = True
  currPos,count,cost=0,1,0

  cProfile.run(f'tspbacktrack1({C}, {currPos},{v}, {n}, {count}, {cost},{[]},{[]})')
  #CODE ẢNH HƯỞNG SỐ CẠNH ĐẾN ĐPT CỦA DYNAMIC PROGRAMMING
n=10
C=createArray2D(n)
s=n*(n-1)
l=50
countEdge=0
print(f'so canh: {l}')
C=generateInputGraph(n,C,l,countEdge)

print(C)
print(dynamic1(C))
cProfile.run(f'dynamic1({C})')
print(C)
for i in range(l+1,s+1):
  print(f'so canh: {i}')
  C=generateInputGraph(n,C,i,i-1)#tăng so canh len 1

  cProfile.run(f'dynamic1({C})')
