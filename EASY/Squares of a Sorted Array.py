class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            x = nums[r]*nums[r]
            y = nums[l]*nums[l]
            if x > y:
                ans[i] = x
                r -= 1
            else:
                ans[i] = y
                l += 1
        return ans
