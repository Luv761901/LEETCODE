class Solution:
    def numTrees(self, n: int) -> int:
        numerator = factorial(2*n)
        denom1 = factorial(n+1)
        denom2 = factorial(n)
        denom = denom1*denom2
        result = numerator//denom
        return result
