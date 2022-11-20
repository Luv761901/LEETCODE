class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        a = sorted(nums)
        for i in range(len(nums)-k):
            nums.remove(a[i])
        return nums
