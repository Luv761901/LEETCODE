class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = ""
        for i in range(1, n+1):
            x = bin(i)[2:]
            ans += x
        m = (10**9)+7
        return (int(ans, 2)) % m
