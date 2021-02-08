def getValue(arr, pos):
  lpos = pos-1
  rpos = pos+1

  while (lpos >= 0):
    if(arr[lpos] != -1):
      break
    lpos -= 1
  while (rpos < len(arr)):
    if(arr[rpos] != -1):
      break
    rpos += 1

  if (lpos < 0):
    lvalue = 1
  else:
    lvalue = arr[lpos]
  if (rpos >= len(arr)):
    rvalue = 1
  else:
    rvalue = arr[rpos]
  
  return arr[pos]*rvalue*lvalue

def Divide(arr, check, l, r):
  #print(l, r)
  if (l > r): return 0
  if (l == r): 
    check[l] = arr[l]
    tmp = getValue(check,l)
    check[l] = -1
    return tmp

  _max = 0
  for i in range(l, r+1):
    check[i] = arr[i]
    #print(arr[i])
    leftValue = Divide(arr, check, l, i-1)
    rightValue = Divide(arr, check, i+1, r)
    #print(arr, check, getValue(check, i), i)
    _max = max(_max, getValue(check, i) + rightValue + leftValue)
    #print(getValue(check, i) + rightValue + leftValue)
    check[i] = -1

  return _max


def remake(arr, ans):
    while 1 in arr:
        pos = arr.index(1)
        if pos == 0:
            ans += arr[pos+1]
        elif pos == len(arr)-1:
            ans += arr[pos-1]
        else:
            ans += arr[pos+1] * arr[pos-1]
        arr.pop(pos)

    return arr, ans

def findMax(arr):
    Max = 0
    pos = 0
    for i in range(0,len(arr)):
        if Max <= arr[i]:
            Max = arr[i]
            pos = i
    return pos, Max

def rotate(arr):
    arr1 = []
    for i in range(len(arr)-1, -1, -1):
        arr1.append(arr[i])
    return arr1
def solve(arr, check):
    ans = 0
    arr1 = []
    arr, ans = remake(arr, 0)
    pos_Max, Max = findMax(arr)
    if pos_Max == 0 or pos_Max == len(arr) -1 :
        if pos_Max == len(arr)-1:
            new_Arr = rotate(arr)
            arr.clear()
            arr = new_Arr

        i = 1
        while i!= len(arr)-1:
            if arr[i]!= Max:
                ans+= arr[i]* arr[i-1]* arr[i+1]
                arr.pop(i)
            else:
                i+=1
        if len(arr)>3:
            j = 1
            while len(arr)>3:
                ans+= arr[j]* arr[j-1]* arr[j+1]
                arr.pop(j)

        if len(arr) == 3:
            return ans + arr[0]* arr[1]*arr[2] + arr[0] * arr[2] + max(arr[0],arr[2])
        elif len(arr)==2:
            return ans + arr[0]* arr[1] +max(arr[0],arr[1])
        elif len(arr)==1:
            return arr[0]+ans
    else:
      return Divide(arr, check, 0, n-1)

n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
check = [-1 for i in range(n)]

if (n < 10):
  print(Divide(arr, check, 0, n-1))
else:
  print(solve(arr, check))
#submit AC 2
def getValue(arr, pos):
  lpos = pos-1
  rpos = pos+1

  while (lpos >= 0):
    if(arr[lpos] != -1):
      break
    lpos -= 1
  while (rpos < len(arr)):
    if(arr[rpos] != -1):
      break
    rpos += 1

  if (lpos < 0):
    lvalue = 1
  else:
    lvalue = arr[lpos]
  if (rpos >= len(arr)):
    rvalue = 1
  else:
    rvalue = arr[rpos]
  
  return arr[pos]*rvalue*lvalue

def Divide(arr, check, l, r):
  #print(l, r)
  if (l > r): return 0
  if (l == r): 
    check[l] = arr[l]
    tmp = getValue(check,l)
    check[l] = -1
    return tmp

  _max = 0
  for i in range(l, r+1):
    check[i] = arr[i]
    #print(arr[i])
    leftValue = Divide(arr, check, l, i-1)
    rightValue = Divide(arr, check, i+1, r)
    #print(arr, check, getValue(check, i), i)
    _max = max(_max, getValue(check, i) + rightValue + leftValue)
    #print(getValue(check, i) + rightValue + leftValue)
    check[i] = -1

  return _max



n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
check = [-1 for i in range(n)]

print(Divide(arr, check, 0, n-1))