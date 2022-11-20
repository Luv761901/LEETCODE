class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def rev(n):
            s = ""
            p = str(n)
            for i in reversed(p):
                s += i
            for i in s:
                if i != '0':
                    break
                else:
                    s = s.replace(i, '')
            return s
        x = rev(num)
        y = rev(x)
        if num == 0:
            return True
        if y == str(num):
            return True
        else:
            return False
