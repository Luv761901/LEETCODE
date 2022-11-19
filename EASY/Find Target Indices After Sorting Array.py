class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(i)
        return a
