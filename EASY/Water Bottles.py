class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        f, e, c = numBottles, numBottles, numBottles
        while(f != 0):
            f = e//numExchange
            c += f
            e = f+(e % numExchange)
        return c
