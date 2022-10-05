class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            s = math.ceil(math.log(n, 3))
            print(s)
            if 3**s == n:
                return True
            else:
                return False
