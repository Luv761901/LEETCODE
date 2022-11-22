class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for i in range(2, num+1):
            sum = 0
            s = str(i)
            for i in s:
                sum += int(i)
            if sum % 2 == 0:
                c += 1

        return c
