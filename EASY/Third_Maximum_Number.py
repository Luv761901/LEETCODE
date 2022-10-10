class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        s = len(list(set(nums)))
        p = sorted(list(set(nums)))
        print(s)
        print(p)
        if s <= 2:
            return max(nums)
        else:
            return p[-3]
