class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = bin(n)[2:]
        s1 = ""
        for i in range(len(x)):
            if x[i] == '1':
                s1 += '0'
            else:
                s1 += '1'
        s = int(s1, 2)
        return s
