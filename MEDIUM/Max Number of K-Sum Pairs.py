class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        d = defaultdict(int)
        for i in nums:
            if d[k-i]:
                d[k-i] -= 1
                count += 1
            else:
                d[i] += 1
        return count
