class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(n)[2:])
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                return False
        return True
