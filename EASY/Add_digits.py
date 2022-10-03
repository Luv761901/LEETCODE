class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        sum1 = 0
        while(1):
            for i in num:
                sum1 += int(i)
            if len(str(sum1)) == 1:
                return int(sum1)
            num = str(sum1)
            sum1 = 0
