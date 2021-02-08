def ternarySearch(l, r, key, ar):
    count=1
    while(r >= l):

        # Find the mid1 and mid2
        mid1 = (r+2*l)//3
        mid2 = ((2*r +l) // 3 )+1

        # Check if key is present at any mid
        if (ar[mid1] == key):

            return [mid1,count]
        if (ar[mid2] == key):
            return [mid2,count]

        # Since key is not present at mid,
        # check in which region it is present
        # then repeat the Search operation
        # in that region
        count+=1

        if (key < ar[mid1]):
            r=mid1-1
            continue
        elif (key > ar[mid2]):
            l=mid2+1
            continue
            # The key lies in between mid2 and r
        else:
            l=mid1+1
            r=mid2-1
            continue
    # Key not found
    return [-1,count]
n=int(input())
a = list(map(int,input().strip().split()))[:n]
m=int(input())
b = list(map(int,input().strip().split()))[:m]
for i in range(0,m):
    arr=ternarySearch(0,len(a)-1,b[i],a)
    print(arr[0],end=" ")
    print(arr[1])