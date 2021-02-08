def longestPalindromeSubseq(s: str) :
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = 1

    for l in range(1, len(s)):
        for i in range(len(s) - l):
            j = i + l
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]
s=input()
print(longestPalindromeSubseq(s))