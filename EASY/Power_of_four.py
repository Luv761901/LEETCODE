class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            s=math.floor(math.log(n,4))
            if 4**s==n:
                return True
            else:
                return False