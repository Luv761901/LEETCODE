class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d = {}
        p = 1
        for i in range(97, 123):
            s2 = chr(i)
            d[s2] = p
            p += 1
        s1 = ""
        for i in s:
            s1 += str(d[i])
        while(k != 0):
            sum1 = 0
            for i in s1:
                sum1 += int(i)
            s1 = str(sum1)
            k -= 1
        return (int(s1))
