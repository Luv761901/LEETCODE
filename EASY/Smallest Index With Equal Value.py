class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                a.append(i)

        if a == []:
            return -1
        else:
            s = min(a)
            return s
