
from random import seed
from random import randint
import copy
def tspbacktrack(C, currPos, v, n, count, lengthSoFar, path, allPaths):# code backtracking
    if count == n:
        minCost = lengthSoFar + C[0][currPos]
        path.append(1)
        allPaths.append((minCost, path[:]))
        path.pop()
    else:
        minCost = float('inf')
        for i in range(n):
            if v[i] == False:
                v[i] = True
                path.append(i+1)
                newDistance = lengthSoFar + C[i][currPos]
                minCost = min(minCost, tspbacktrack(
                    C, i, v, n, count + 1, newDistance, path, allPaths))
                path.pop()
                v[i] = False
    return minCost
def findPath(C):#traceback 
    v = [False for i in range(len(C))]
    v[0] = True
    path = [1]
    allPaths = []
    infinity = float('inf')
    minCost = tspbacktrack(C, 0, v, len(C), 1, 0, path, allPaths)
    if minCost == infinity:
         return []
    for t in allPaths:
        if t[0] == minCost:
            return t[1]




#code bỏ qua các đường đi không tồn tại
def tspbacktrack1(C, currPos, v, n, count, lengthSoFar, path, allPaths):
    notWay=float('inf')
    if (count == n and C[currPos][0] !=0 and C[currPos][0]!=float('inf')):
        minCost = lengthSoFar + C[0][currPos]
        path.append(1)
        allPaths.append((minCost, path[:]))
        path.pop()
    else:
        minCost = float('inf')
        for i in range(n):
            if (v[i] == False and C[currPos][i]!=0 and C[currPos][i]!=notWay):
                v[i] = True
                path.append(i+1)
                newDistance = lengthSoFar + C[i][currPos]
                minCost = min(minCost, tspbacktrack(
                    C, i, v, n, count + 1, newDistance, path, allPaths))
                path.pop()
                v[i] = False
    return minCost


def findPath1(C):
    v = [False for i in range(len(C))]
    v[0] = True
    path = [1]
    allPaths = []
    minCost = tspbacktrack(C, 0, v, len(C), 1, 0, path, allPaths)
    for t in allPaths:
        if t[0] == minCost:
            return t[1]
