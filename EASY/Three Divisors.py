class Solution:
    def isThree(self, n: int) -> bool:
        a = []
        for i in range(1, n+1):
            if n % i == 0:
                a.append(i)
        if len(a) == 3:
            return True
        else:
            return False
