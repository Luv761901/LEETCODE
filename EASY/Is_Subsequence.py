class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        elif len(s) > len(t):
            return False
        else:
            c = 0
            for i in range(len(t)):
                if c <= len(s)-1:
                    if s[c] == t[i]:
                        c += 1
            if c == len(s):
                return True
            return False
