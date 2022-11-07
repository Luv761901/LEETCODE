class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ans = []
        for i in nums:
            ans.append(i)
            if sum(ans) > (sum(nums)-sum(ans)):
                break
        return ans
