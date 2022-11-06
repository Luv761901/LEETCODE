class Solution:
    def numberOfSteps(self, num: int) -> int:
        temp=num
        c=0
        while(temp):
            if temp%2==0:
                temp//=2
                c+=1
                continue
            else:
                temp-=1
                c+=1
        return c        