class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check(arr):
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    return 0
            return 1
        if check(nums) == True:
            return True
        for i in range(len(nums)):
            x = nums[:i]+nums[i+1:]
            if sorted(x) == x:
                if len(set(x)) == len(x):
                    return True
        return False
