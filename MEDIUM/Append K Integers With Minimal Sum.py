class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums=sorted(set(nums))
        f_sum=k*(k+1)//2
        for i in nums:
            if i<=k:
                f_sum+=k-i+1
                k+=1
            else:
                break
        return f_sum