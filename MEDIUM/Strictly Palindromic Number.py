class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, (n-2)+1):
            x = bin(i)[2:]
            if x == x[::-1]:
                continue
            else:
                return False
        return True
