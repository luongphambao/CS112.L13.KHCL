# chương trình tạo dữ liệu trong TH không đồ thị không đầy đủ (không có đường đi trực ở 2 thành phố nào đó)
from random import seed
from random import randint
import copy
def InputGraph(n,l):#n là số thành phố,l là số đường đi (đường đi từ A đến B khác từ A đến B)
  notWay= float('inf') 
  countEdge = 0
  C=[]
  for i in range(n):
    arr=[notWay if j != i else 0 for j in range(n)]
    C.append(arr)
  while(countEdge<l):
    A=randint(1,n)
    B=randint(1,n)
    value=randint(1,1000)
    DistanceAtoB=C[A-1][B-1]
    if A!=B and DistanceAtoB ==notWay:
      C[A-1][B-1]=value
      countEdge+=1
  return C
def generateInputGraph(n,C,l,countEdge): #l là số cạnh mong muốn,countEdge để đếm số lượng cạnh hiện tại
    notWay= float('inf') 
    while(countEdge<l):
      A=randint(1,n)
      B=randint(1,n)
      value=randint(1,1000)
      DistanceAtoB=C[A-1][B-1]
      if A!=B and DistanceAtoB ==notWay:
        C[A-1][B-1]=value
        countEdge+=1
      
    return C
def createArray2D(n):#tạo mảng 2 chiều 
    notWay= float('inf') 
    arr2d=[]
    for i in range(n):
      arr=[notWay for i in range(n)]
      arr2d.append(arr)
    return arr2d