class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        else:
            p = 2*original
            while p in nums:
                p = 2*original
                original = p
            return p
