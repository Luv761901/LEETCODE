class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s = s | i
        return s*2**(len(nums)-1)
