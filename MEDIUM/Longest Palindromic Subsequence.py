class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2 = s1[::-1]
        n = len(s1)
        m = len(s2)
        if n == 0 or m == 0:
            print(0)
        else:
            dp = [[0 for j in range(m+1)]for i in range(n+1)]
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return (dp[n][m])
