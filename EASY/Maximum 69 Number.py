class Solution:
    def maximum69Number(self, num: int) -> int:
        s = list(str(num))
        p = 0
        while(p < len(s)):
            if s[p] == '6':
                s[p] = '9'
                break
            p += 1
        ans = ""
        ans = ans.join(s)
        return int(ans)
