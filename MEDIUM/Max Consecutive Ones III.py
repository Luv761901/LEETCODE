class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ws = 0
        m = -math.inf
        for we in range(len(nums)):
            if nums[we] == 0:
                k -= 1
            while (k < 0):
                if nums[ws] == 0:
                    k += 1
                ws += 1
            m = max(m, we-ws+1)
        return m
