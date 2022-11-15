class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = [0]*len(s)
        print(s)
        for i in s:
            x = int(i[-1])
            ans[x-1] = i[:len(i)-1]
        res = " "
        res = res.join(ans)
        return res
