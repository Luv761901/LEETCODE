class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = [0]
        for i in nums:
            p.append(p[-1]+i)
        d = {}
        ans = 0
        for i in p:
            if i-k in d:
                ans += d[i-k]
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return ans
