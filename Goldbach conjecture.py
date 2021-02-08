def prime(n):
    f=[1 for i in range(0,n+1)]
    f[0]=0
    f[1]=0
    s=int(n**0.5)+1
    for i in range(2,s):
        if f[i]==1:
            for j in range(2*i,n+1,i):
                f[j]=0
    arr=[]
    for i in range(2,n+1):
        if f[i]==1:
            arr.append(i)
    return arr


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


n=int(input())
arr=prime(n)
count=0
s1=len(arr)
a1=[]

for i in range(0,s1):
    s=n-arr[i]
    index=binary_search(arr,i,s1-1,s)
    if index>=0:
        if s<arr[i]:
            break
        else:
            count+=1



print(count)