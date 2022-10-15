class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        s = 1
        p = int(math.sqrt(num))
        for i in range(2, p+1):
            if num % i == 0:
                s += i+num//i
        if s == num:
            return True
        else:
            return False
