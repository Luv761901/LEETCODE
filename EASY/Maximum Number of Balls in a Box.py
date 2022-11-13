class Solution:
    def countBalls(self, x: int, y: int) -> int:
        def sumDigit(num):
            s = 0
            p = str(num)
            for i in p:
                s += int(i)
            return s
        d = {}
        for i in range(x, y+1):
            s = sumDigit(i)
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return max(d.values())
