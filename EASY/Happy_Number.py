class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        sum = 0
        while (1):
            for i in n:
                sum += int(i)*int(i)
            if sum == 1 or sum == 7:
                return True
            if 2 <= sum <= 9:
                return False

            n = str(sum)
            sum = 0
