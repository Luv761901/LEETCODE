class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        print(a)
        for i in range(len(a)):
            a[i] = a[i][::-1]
        s = " ".join(a)
        return s
