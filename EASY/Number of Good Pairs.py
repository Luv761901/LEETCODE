class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for number in nums:
            if number in d:
                res += d[number]
                d[number] += 1
            else:
                d[number] = 1
        return res
