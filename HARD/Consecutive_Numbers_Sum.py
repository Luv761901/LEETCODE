class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        k = 1
        c = 0
        while (k*(k+1)//2) <= n:
            sk = k*(k+1)//2
            if (n-sk) % k == 0:
                c += 1
            k += 1
        return c
