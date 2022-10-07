class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wsum = 0
        ws = 0
        minsize = math.inf
        for we in range(len(nums)):
            wsum += nums[we]
            while wsum >= target:
                minsize = min(minsize, we-ws+1)
                wsum -= nums[ws]
                ws += 1
        if minsize == math.inf:
            return 0
        return minsize
