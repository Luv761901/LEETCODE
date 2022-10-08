class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            Max = 0
            for j in range(i):
                if nums[i] > nums[j] and dp[j] > Max:
                    Max = dp[j]
            dp[i] = Max+1
            ans = max(ans, dp[i])
        return ans
