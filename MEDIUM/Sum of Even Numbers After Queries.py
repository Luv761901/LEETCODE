class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        m = 0
        for i in nums:
            if i % 2 == 0:
                m += i
        for i in queries:
            s = i[0]
            t = i[1]
            if nums[t] % 2 == 0:
                m -= nums[t]
            nums[t] += s
            if nums[t] % 2 == 0:
                m += nums[t]
            ans.append(m)
        return ans
