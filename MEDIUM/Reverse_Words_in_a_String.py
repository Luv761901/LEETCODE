class Solution:
    def reverseWords(self, s: str) -> str:
        op = s.split()
        print(op)
        s1 = ""
        for i in reversed(op):
            s1 += i
            s1 += " "
        return s1.strip()
