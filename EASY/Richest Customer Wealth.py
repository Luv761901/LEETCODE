class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = 0
        for i in accounts:
            p = sum(i)
            if p > sum1:
                sum1 = p
        return sum1
