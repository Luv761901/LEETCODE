class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            ans = ans ^ (start+2*i)
        # print(nums)
        # ans=nums[0]
        # for i in range(1,n):
        #     ans=nums[i]^ans
        return ans
