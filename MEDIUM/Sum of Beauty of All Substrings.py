class Solution:
    def beautySum(self, s: str) -> int:
        def b(S):
            p = dict(Counter(S))
            a = sorted(p.values())
            return a[-1]-a[0]
        Sum = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                c = b(s[i:j])
                Sum += c
        return Sum
