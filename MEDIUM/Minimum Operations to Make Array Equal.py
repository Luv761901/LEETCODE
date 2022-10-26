class Solution:
    def minOperations(self, n: int) -> int:
        a = []
        for i in range(n):
            a.append(2*i+1)
        l = 0
        r = n-1
        s = 0
        while(l < r):
            s += (a[r]-a[l])//2
            l += 1
            r -= 1
        return s
