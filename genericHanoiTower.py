#tìm vị trí i,j của đĩa số x trên đỉnh các cột trong tháp
def find(array, x):
  for i in range(len(array)):
    if len(array[i])>0:
      j = len(array[i])-1
      if array[i][j]==x:
        return i,j

#đây là hàm chuyển đổi n đĩa từ 1 cột thứ a sang cột thứ c và lấy cột thứ b làm trung gian
def arrangeTower(array,n,a,b,c):
  if n == 1:
    #in ra mảng sau khi pop và append
    array[c].append(array[a].pop())
    for i in range(len(array)):
      for j in range(len(array[i])):
        print(array[i][j], end=' ')
      print()
    print('#')
    return
  arrangeTower(array,n-1,a,c,b)
  arrangeTower(array,1,a,b,c)
  arrangeTower(array,n-1,b,a,c)


def solveTower(array):
  #tìm vị trí của đĩa bắt đầu 0
  x,y = find(array,0)
  #nếu có một đoạn các đĩa đã xếp sẵn trong cột thì lấy vị trí x,y mới và tính số đĩa đã xếp n
  while y>0:
    if (array[x][y-1]-array[x][y])==1:
      y-=1
    else:
      break
  n = len(array[x])-y

  #tìm lần lượt từ đĩa bé đến đĩa lớn để xếp lên nhau
  t = len(array[0])+len(array[1])+len(array[2])
  while n<t:
    #xét tìm phần tử tiếp theo chưa xếp trên đỉnh cột h
    h,k = find(array,n)
    #xác định cột temp[0] trung gian
    temp = [0,1,2]
    temp.remove(x)
    temp.remove(h)
    #chuyển 1 đĩa trên đỉnh cột h qua cột trung gian temp
    arrangeTower(array,1,h,x,temp[0])
    #xác định lại y
    y = len(array[temp[0]])-1
    #chuyển n đĩa đã xếp sẵn ở cột x qua cột trung gian temp
    arrangeTower(array,n,x,h,temp[0])
    #xác định lại x
    x=temp[0]
    #nếu có một thêm 1 đoạn các đĩa đã xếp sẵn trong cột temp thì lấy vị trí y mới và tính thêm số đĩa đã xếp n
    while y>0:
      if (array[x][y-1]-array[x][y])==1:
        y-=1
      else:
        break
    n = len(array[x])-y

  #xử lý nếu cột đã xếp xong mà chưa đúng là cột thứ 3
  if x!=2:
    temp = [0,1,2]
    temp.remove(x)
    temp.remove(2)
    arrangeTower(array,n,x,temp[0],2)

array = []
array.append([int(i) for i in input().split()])
array.append([int(i) for i in input().split()])
array.append([int(i) for i in input().split()])

#in ra trước khi xếp
for i in range(len(array)):
  for j in range(len(array[i])):
    print(array[i][j], end=' ')
  print()
print('#')

solveTower(array)