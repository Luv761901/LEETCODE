class Solution:
    def isMatch(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        dp = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and s2[j-1] == '*':
                    dp[i][j] = dp[i][j-1]
                elif i == 0 or j == 0:
                    dp[i][j] = False
                elif s1[i-1] == s2[j-1] or s2[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif s2[j-1] == '*':
                    dp[i][j] = (dp[i-1][j] or dp[i][j-1])
                else:
                    dp[i][j] = False
        return (dp[n][m])
