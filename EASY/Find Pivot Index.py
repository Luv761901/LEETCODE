class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        l = 0
        for i in range(len(nums)):
            s = s-nums[i]
            if l == s:
                return i
            l = l+nums[i]
        return -1
