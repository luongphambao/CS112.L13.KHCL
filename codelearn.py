def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1
  
def missingNumber(arr,k):
    min1=min(arr)
    max1=max(arr)
    count=0
    index=0
    for i in range(min1+1,max1):
        index1=binarySearch(arr,index,len(arr)-1,i)
        if index1==-1:
            count+=1
        else:
            index=index1
        if count==k:
            return i-1
    if count<=k:
        return i+k-count+1
arr=[3, 2, 4, 7, 8, 10, 860, 1, 560, 842]
k=3
print(missingNumber(arr,k))
#loi giai thu 1
# minh la mot con meo ngu ngoc
sum1=0 
for i in range(10):
    sum1+=1 
print(sum1)
#con meo ngu ngoc