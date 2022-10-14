class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1] == 0):
                return True
        d = defaultdict(int)
        d[0] = 1
        for i in nums:
            s = (s+i) % k
            if (i and s) in d and (d[s] >= 2 or i % k):
                return True
            d[s] += 1
        return False
