from functools import reduce


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        c = 0
        m = max(nums)
        for i in nums:
            if i == m:
                c += 1
            else:
                c = 0
            l = max(l, c)
        return l
