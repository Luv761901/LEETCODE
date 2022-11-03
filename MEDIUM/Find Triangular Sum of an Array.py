class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] % 10
        else:
            n = len(nums)
            a = nums[:]
            while(n != 1):
                temp = [0]*(n-1)
                for i in range(n-1):
                    temp[i] = (a[i]+a[i+1]) % 10
                a = temp[:]
                n -= 1
            return temp[-1]
