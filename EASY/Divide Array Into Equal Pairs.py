class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        s = len(nums) // 2
        count = 0
        for i in range(0, len(nums), 2):
            for j in range(len(nums)):
                if i == j-1:
                    if nums[i] == nums[j]:
                        count += 1
        if count == s:
            return True
        else:
            return False
