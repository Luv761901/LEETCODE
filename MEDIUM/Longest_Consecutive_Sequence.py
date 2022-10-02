class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        c = 0
        for i in nums:
            if i-1 not in s:
                temp = 0
                while i in s:
                    temp += 1
                    i += 1
                c = max(c, temp)
        return c
