class Solution:
    def isMatch(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        dp = [[False for j in range(m+1)]for i in range(n+1)]
        dp[0][0] = True
        for i in range(1,m+1):
            if s2[i-1] == '*' and i > 1:
                dp[0][i] = dp[0][i-2]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1] or s2[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]   
                elif j>1 and s2[j-1]=="*":    
                    if  s2[j-2] =='.' or s1[i-1]==s2[j-2]:
                        dp[i][j] =dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                    
        return (dp[n][m])