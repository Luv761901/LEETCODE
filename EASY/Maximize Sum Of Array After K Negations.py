class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while(k != 0):
            s = min(nums)
            p = nums.index(s)
            nums[p] = s*-1
            k -= 1
        return sum(nums)
