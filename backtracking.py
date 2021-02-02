from dp import dynamic
from generateInput1 import generate_input
from backtracking import tspbacktrack
import sys
import copy
import random
import cProfile
import time
from random import seed
from random import randint
import copy
#code đo thời gian chạy dynamic programming
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
#code đo thời gian chạy của backtracking
for s in range(4,12):
    print(s)
    getData=generate_input(s,1)
    for i in range(len(getData)):
        graph=getData[i]
        n=int(s)
        v = [False for i in range(n)] 
        v[0] = True
        answer=[]
        matrix=graph
        cProfile.run(f'tspbacktrack({graph},{0},{v},{n},{1},{0},{[]},{[]})')
