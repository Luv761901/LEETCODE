class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        ans = []
        d = {}
        changed.sort(reverse=True)
        for i in changed:
            if i*2 in d:
                ans.append(i)
                if d[i*2] == 1:
                    del d[i*2]
                else:
                    d[i*2] -= 1
            else:
                d[i] = d.get(i, 0)+1
        if len(ans) == len(changed)//2:
            return ans
        return []
