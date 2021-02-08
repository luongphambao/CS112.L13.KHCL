n=int(input())//10000
def coinChange(n):
    if n<2:
        return 0
    mod=10**9+7
    A=[2,5,10,20,50]
    dp=[mod for i in range(n+1)]
    for i in range(2,n+1):
        if i in A:
            dp[i]=1
            continue
        else:
            B=[dp[i-x] for x in A if i>=x]
            dp[i]=min(y for y in B)+1
    if dp[n]==mod+1:
        return 0
    return dp[n]
print(coinChange(n))