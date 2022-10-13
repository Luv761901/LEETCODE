class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        s = ""
        for i in x:
            if i == '1':
                s += '0'
            else:
                s += '1'
        return int(s, 2)
