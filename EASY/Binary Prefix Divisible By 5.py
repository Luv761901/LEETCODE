class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [0]*len(nums)
        s = ""
        for i in range(len(nums)):
            s += str(nums[i])
            if int(s, 2) % 5 == 0:
                ans[i] = True
            else:
                ans[i] = False
        return ans
