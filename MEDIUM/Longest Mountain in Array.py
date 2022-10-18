class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        m = 0
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                x = i-1
                y = i+1
                while(x >= 0):
                    if nums[x] < nums[x+1]:
                        x -= 1
                    else:
                        break
                while(y <= len(nums)-1):
                    if nums[y] < nums[y-1]:
                        y += 1
                    else:
                        break
                m = max(m, y-x-1)
        return m
