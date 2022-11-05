class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c, res = bin(num2)[2:].count('1'), 0
        r1 = 30
        for i in range(r1, -1, -1):
            m = 1 << i
            p = num1 & m
            if p and (c > 0):
                res = res | m
                c -= 1
        i = 0
        while(c > 0):
            m = 1 << i
            if (res & m) == 0:
                res = res | m
                c -= 1
            i += 1
        return res
