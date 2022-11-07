class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i]+nums[i-1]
        print(nums)
        x = min(nums)
        if x <= 0:
            return 1-x
        else:
            return 1
