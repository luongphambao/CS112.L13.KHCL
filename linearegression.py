#sử dụng LinearRegression để phân tích
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("dataset.csv")
data.columns = ['times', 'operations']
data

X_ = np.array(data['times']).reshape(-1, 1)
X_

Y_ = np.array(data['operations']).reshape(-1, 1)
Y_

def nlog2_n(arr):
    return arr*np.log2(arr)
nlog2_n(X_)

def log2_n(arr):
  return np.log2(arr)
log2_n(X_)

def _n(arr):
  return arr

def _n2(arr):
  return arr**2
_n2(X_)

def _n3(arr):
  return arr**3

def _twopown(arr):
  return 2**arr
_twopown(X_)

def npow2mul2pown(arr):
  return (arr**2)*(2**arr)
npow2mul2pown(X_)

def sqrt_n(arr):
  return arr ** (1/2)
sqrt_n(X_)

def tinhgiaithua(n):
    n=n[0]
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;

print(len(X_))
print(X_[0][0])

def giaithua(arr):
  giaithuaArr=[]
  for i in range(len(arr)):
      giaithuaArr.append(tinhgiaithua(arr[i]))
  return np.array(giaithuaArr).reshape(-1, 1)

giaithua(X_)

model = LinearRegression()

model.fit(nlog2_n(X_), Y_)

model.coef_ # a trong y = ax + b

model.intercept_ # b trong y = ax + b