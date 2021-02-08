def kth(a1,m,a2,n,k):
    if (k > (m+n) or k < 1):
        return -1
    if (m > n):
        return kth(a2, n, a1, m, k)
    if (m == 0):
        return a2[k - 1]
    
    if (k == 1):
        return min(a1[0], a2[0])
    
    i = min(m, k // 2) 
    j = min(n, k //2)

    if (a1[i - 1] > a2[j - 1] ): 
        return kth(a1, m, a2 [j:], n - j, k - j)
    else:
        return kth(a1[i:], m - i, a2, n, k - i)
v=int(input())
for i in range(0,v):
    n,m,k=map(int,input().split())
    a = list(map(int,input().strip().split()))[:n]
    b = list(map(int,input().strip().split()))[:m]
    print(kth(a,n,b,m,k+1))