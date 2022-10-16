class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        dp = [[0 for i in range(n)]for j in range(n)]
        for g in range(n):
            i = 0
            j = g
            while(j < n):
                if g == 0:
                    dp[i][j] = 1
                    c += 1
                elif g == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        c += 1
                else:
                    if s[i] == s[j]:
                        if dp[i+1][j-1] == 1:
                            dp[i][j] = 1
                            c += 1

                i += 1
                j += 1
        return c
