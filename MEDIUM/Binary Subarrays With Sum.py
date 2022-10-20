class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p = [0]
        for i in nums:
            p.append(p[-1] + i)
        print(p)
        ans = 0
        d = {}
        for i in p:
            extra = i-goal
            if extra in d:
                ans += d[extra]
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return ans
