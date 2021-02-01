from itertools import permutations
def tsplietke(C,n): #C là đồ thị vô hướng(hoặc có hướng) biễu diễn khoảng cách giữa các thành phố (ARRAY 2 chiều), n là số thành phố
  s=[1]
  arr=[i+2 for i in range(n-1)]
  permut=[]
  permut1=(list(permutations(arr)))
  for i in permut1:
      i=list(s+list(i))
      permut.append(i)
  
  for i in range(len(permut)):
    permut[i]=list(permut[i])
    permut[i].append(1)

  permutCost=[]
  s1=len(permut[0])
  for i in range(0,len(permut)):
    costBtoA=0
    for j in range(1,s1):
      A=permut[i][j-1]
      B=permut[i][j]
      costBtoA+=C[A-1][B-1]
    permutCost.append(costBtoA)
  for i in range(len(permut)):
    permut[i].reverse()
  return permut,permutCost