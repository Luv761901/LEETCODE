class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = list(bin(x)[2:])
        b = list(bin(y)[2:])
        c = 0
        if len(a) < len(b):
            i = 0
            while(len(a) != len(b)):
                a.insert(i, '0')
        elif len(b) < len(a):
            j = 0
            while(len(b) != len(a)):
                b.insert(j, '0')
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        return c
