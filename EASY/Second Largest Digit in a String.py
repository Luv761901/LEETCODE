class Solution:
    def secondHighest(self, s: str) -> int:
        a = []
        for i in s:
            if ord(i) >= 48 and ord(i) <= 57:
                a.append(int(i))
        s1 = list(set(a))
        s1.sort()
        print(s1)
        if len(s1) == 0 or len(s1) == 1:
            return -1
        else:
            return s1[-2]
