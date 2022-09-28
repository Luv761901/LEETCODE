class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            
        def generateSubsets(nums, res, curr, index):
            res.append(list(curr))
            for i in range(index, len(nums)):
                curr.append(nums[i])
                generateSubsets(nums, res, curr, i + 1)
                curr.pop()
        res = []
        generateSubsets(nums, res, [], 0)
        return res