class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c, c1 = 0, 0
        ans = 0
        for i in range(len(s)):
            if s[i] == 'R':
                c += 1
            else:
                c1 += 1
            if c == c1:
                ans += 1
        return ans
