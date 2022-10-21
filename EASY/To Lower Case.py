class Solution:
    def toLowerCase(self, s: str) -> str:
        s1 = ""
        for i in s:
            if i.isupper():
                s1 += i.lower()
            else:
                s1 += i
        return s1
