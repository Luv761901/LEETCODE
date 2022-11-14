class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        n = len(nums)
        for i in range(n):

            if nums[i] > nums[(i+1) % n]:
                c += 1
        if c == 0 or c == 1:
            return True
        return False
