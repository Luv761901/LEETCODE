class Solution:
    def maxPower(self, s: str) -> int:
        i, m = 0, 0
        while i < len(s):
            j = 1
            while i+j < len(s) and s[i+j] == s[i]:
                j += 1
            m = max(m, j)
            i += 1
        return m
