class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = max(nums)
        flag = 0
        for i in nums:
            if i == x:
                continue
            else:
                if i*2 > x:
                    flag = -1
                    break
        if flag == 0:
            return nums.index(x)
        else:
            return flag
