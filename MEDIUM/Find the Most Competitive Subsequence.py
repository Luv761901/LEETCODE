class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        no = n-k
        stack = []
        if no == 0:
            return nums
        for i in range(len(nums)):
            while len(stack) != 0 and stack[-1] > nums[i] and no > 0:
                stack.pop()
                no -= 1
            stack.append(nums[i])
        while no > 0:
            stack.pop()
            no -= 1
        return stack
        return stack
