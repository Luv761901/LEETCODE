class Solution:
    def minimumSum(self, num: int) -> int:
        s = list(str(num))
        s.sort()
        print(s)
        a = s[0]+s[2]
        b = s[1]+s[3]
        return (int(a)+int(b))
