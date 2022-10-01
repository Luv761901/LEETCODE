class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n).replace("0b", "")
        while(len(s) != 32):
            s = '0'+s
        p = s[::-1]
        return int(p, 2)
