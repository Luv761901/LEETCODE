class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws = 0
        wsum = 0
        maxavg = -math.inf
        for we in range(len(nums)):
            wsum += nums[we]
            if we >= k-1:
                maxavg = max(maxavg, wsum/k)
                wsum -= nums[ws]
                ws += 1
        return maxavg
