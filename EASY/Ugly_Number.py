class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            while n%3==0:
                n=n/3
            while n%5==0:
                n=n/5
            while n%2==0:
                n=n/2
            if n==1:
                return True
            else:
                return False