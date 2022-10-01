class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        max1 = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = max(d.values())
        for i in d:
            if d[i] == m:
                return i
