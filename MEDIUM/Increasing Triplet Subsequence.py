class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3 or len(set(nums))<3:
            return False
        i,j,k=0,1,2
        n=len(nums)
        while k<n or j<n-1:
            if nums[j]<=nums[i]:
                i=i+1
                j=i+1
                k=j+1
            else:
                if nums[k]>nums[j]:
                    return True
                else:
                    k=k+1
                    if k==n:
                        j=j+1
                        k=j+1
        return False