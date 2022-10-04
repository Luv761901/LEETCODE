class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s = max(nums)
        return nums.index(s)
