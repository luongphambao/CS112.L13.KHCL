def solve(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i,j=0,0
    arr=[]
    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    arr+=arr1[i:]+arr2[j:]

    n1=len(arr)
    if n1%2==0:
        s=(arr[n1 // 2] + arr[n1 // 2 - 1]) / 2
        if s==int(s):
            return int(s)
        return s
    return arr[n1//2]
n=int(input())
for i in range(0,n):
    s1,s2=map(int,input().split())
    a = list(map(int,input().strip().split()))[:s1]

    b = list(map(int,input().strip().split()))[:s2]
    print(solve(a,b))