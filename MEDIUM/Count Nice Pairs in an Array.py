class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        c = 0
        a = []

        def rev(x):
            s = ""
            p = str(x)
            for i in reversed(p):
                s += i
            return int(s)
        for i in range(len(nums)):
            a.append(nums[i]-rev(nums[i]))
        print(a)
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        for i in d:
            m = d[i]*(d[i]-1)/2
            c += m
        return int(c) % (10**9+7)
