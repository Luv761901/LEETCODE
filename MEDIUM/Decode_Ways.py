class Solution:
    def numDecodings(self, s: str) -> int:
        def solve(s1, i, dp):
            if dp[i] != -1:
                return dp[i]
            if i >= len(s1):
                return 1
            elif s1[i] == '0':
                return 0
            left = solve(s1, i+1, dp)
            right = 0
            num = int(s1[i:i+2])
            if num >= 10 and num <= 26 and i < len(s1)-1:
                right = solve(s1, i+2, dp)
            dp[i] = left+right
            return dp[i]

        dp = [-1 for i in range(len(s)+1)]
        ans = solve(s, 0, dp)
        return ans
