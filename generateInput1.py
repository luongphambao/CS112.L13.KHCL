# Chương trình sinh dữ liệu trong TH đồ thị đầy đủ (giữa các thành phố luôn tồn tại đường đi)
import sys
import copy
import random
import cProfile
import time
from random import seed
from random import randint
import copy
#import các thư viện cần thiết
# Chương trình sinh dữ liệu trong TH đồ thị đầy đủ (giữa các thành phố luôn tồn tại đường đi)
def generate_input(n,k):# n là số thành phố,k là số bộ dữ liệu muốn tạo ra
  data=[]
  for i in range(0,k):
    n=int(n)
    graph_generate=generate(n)
    data.append(graph_generate)
    
  return data
#hàm tạo 1 bộ dữ liệu ngẫu nhiên có kích thước n
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
