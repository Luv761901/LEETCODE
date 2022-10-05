class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        accu_val=0
        n=len(nums)
        for i in range(n+1):
            accu_val+=i
        for i in nums:
            accu_val-=i
        return accu_val    