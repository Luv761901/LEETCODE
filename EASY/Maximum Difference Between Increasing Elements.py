class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    a.append(nums[j]-nums[i])
        print(a)
        if len(a) == 0:
            return -1
        return max(a)
