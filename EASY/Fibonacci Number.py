class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        A = [1]
        temp = n
        while(temp != 0):
            c = a+b
            a = b
            b = c
            A.append(c)
            temp -= 1
        s = n-1
        if n == 0:
            return 0
        return A[s]
