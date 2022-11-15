class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = ""
        S = s.split()
        p = 0
        while (p < k):
            res += S[p]
            res += " "
            p += 1
        print(res)
        return res[:-1]
