class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            a, b = [], []
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    a.append(nums[i])
                else:
                    b.append(nums[i])
            return a+b
