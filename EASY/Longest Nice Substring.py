class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        m = ""
        a = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                a.append(s[i:j])
        print(a)
        for i in a:
            f = 0
            for j in range(len(i)):
                if i[j].isupper():
                    if chr(ord(i[j])+32) not in i:
                        f = -1
                        break
                elif i[j].islower():
                    if chr(ord(i[j])-32) not in i:
                        f = -1
                        break
            if f != -1:
                if len(i) > len(m):
                    m = i
        return m
