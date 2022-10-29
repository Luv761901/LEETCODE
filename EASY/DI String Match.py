class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0
        r = len(s)
        ans = []
        for i in s:
            if i == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        ans.append(r)
        return ans
