import random
import cProfile
import time
from random import seed
from random import randint
import copy
from dp import dynamic
from generateInput1 import generate_input
from backtracking import tspbacktrack
import sys
#So sánh kết quả DP và backtracking
for s in range(4,9):
    getData=generate_input(s,1)
    for i in range(len(getData)):
              graph=getData[i]
              n=int(s)
              v = [False for i in range(n)] 
              v[0] = True
              answer=[]
              matrix=graph
              print(f'Bo du lieu voi kich thuoc n={n}')
              print(f'Ket qua backtracking:{tspbacktrack(graph,0,v,len(graph),1,0,[],[])}')
              print(f'Ket qua dynamic programming: {dynamic(matrix)}')