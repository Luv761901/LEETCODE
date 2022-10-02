class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)[2:]
        p=str(s)
        c=0
        for i in range(len(p)):
           if p[i]=='1':
             c+=1
        return c    