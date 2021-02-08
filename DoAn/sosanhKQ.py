import random
import cProfile
import time
from random import seed
from random import randint
import copy
from dp import dynamic
from generateInput2 import InputGraph
from backtracking import tspbacktrack
from lietke import tsplietke
from backtracking import findPath
import sys
C = InputGraph(4,8 )
print(C)
arr1,arr2=(tsplietke(C,4))
infinity = float('inf')
for i in range(len(arr1)): #in ra các đường đi với chi phí
    if arr2[i] != infinity:
        print(f'Thu tu duong di {arr1[i]}') 
        print(f'Chi phi: {arr2[i]}')
v=[False for i in range(len(C))]
v[0] = True
minPath = findPath(C)
if len(minPath) != 0:
  print('Duong di nho nhat su dung backtracking:' ,*minPath)
  print('Duong di nho nhat su dung DP:')
  path, minCost = dynamic(C)
  print('Duong di dp:', *path)
  print('Do dai dp:', minCost)
else:
  print('Khong co duong di')
