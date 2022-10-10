class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = []
        p, x = 0, 0
        sum1, sum2 = 0, 0
        for i in reversed(num1):
            sum1 += (10**p)*int(i)
            p += 1
        a.append(sum1)
        for i in reversed(num2):
            sum2 += (10**x)*int(i)
            x += 1

        a.append(sum2)
        print(a)
        return str(sum(a))
