class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n+1):
            c = bin(i)[2:]
            a.append(c.count('1'))
        return a
