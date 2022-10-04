class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if(nums[0] <= nums[len(nums)-1]):
            return nums[0]
        while(l <= r):
            mid = (l+r)//2
            if(nums[mid] < nums[mid-1]):
                return nums[mid]
            elif(nums[mid] < nums[0]):
                r = mid-1
            else:
                l = mid+1
