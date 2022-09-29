class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        else:
            start = 0
            end = prices[0]
            for i in range(len(prices)):
                ans = prices[i]-end
                start = max(ans, start)
                end = min(end, prices[i])
            return start
