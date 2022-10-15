class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        if num == 0:
            return "0"
        if num < 0:
            temp = abs(num)
        else:
            temp = num
        while(temp > 0):
            s += str(temp % 7)
            temp = temp//7
        if num < 0:
            s = s[::-1]
            z = (-1)*int(s)
            return str(z)
        else:
            return str(s[::-1])
