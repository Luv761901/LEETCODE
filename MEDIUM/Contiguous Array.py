class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            if nums[i] == 1:
                count += 1
            if count in d:
                ans = max(ans, i-d[count])
            else:
                d[count] = i
        return ans
