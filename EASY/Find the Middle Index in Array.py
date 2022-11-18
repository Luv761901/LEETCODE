class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        flag = 0
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[1:]) == 0:
                    return 0
            if i == len(nums)-1:
                if sum(nums[:len(nums)-1]) == 0 and len(nums) != 2:
                    return len(nums)-1
                else:
                    flag = -1
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        if flag == -1:
            return -1
