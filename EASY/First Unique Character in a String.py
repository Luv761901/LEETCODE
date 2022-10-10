class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        p = ""
        flag = 0
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] == 1:
                flag += 1
                p += i
                break
        if flag == 0:
            return -1
        else:

            z = s.index(p)
            return z
