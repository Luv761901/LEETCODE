class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = 1
        s = 0
        for i in nums:
            if i != 0:
                n *= i
            else:
                s += 1
                if s > 1:
                    return [0]*len(nums)
        print(n)
        if s == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = n
        else:
            for i in range(len(nums)):
                nums[i] = n//nums[i]
        return nums
