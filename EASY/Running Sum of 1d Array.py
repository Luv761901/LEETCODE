class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            a.append(sum1)
        return a
