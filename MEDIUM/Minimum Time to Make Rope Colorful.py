class Solution:
    def minCost(self, s: str, neededTime: List[int]) -> int:
        ans = 0
        m = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                m = 0
            ans += min(m, neededTime[i])
            m = max(m, neededTime[i])
        return ans
