class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return (dp[n][m])
