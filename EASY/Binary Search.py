class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        loc = -1
        end = len(nums)-1
        while(start <= end):
            mid = (start+end)//2
            if nums[mid] == target:
                loc = mid
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return loc
