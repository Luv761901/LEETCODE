class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        p = [0]
        for i in nums:
            p.append(p[-1]+i)
        p.remove(p[0])
        print(p)
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = (p[-1]-p[i])-(nums[i]*(n-1-i))
                ans.append(left+right)
            elif i == n-1:
                left = nums[i]*i-(p[i-1])
                right = 0
                ans.append(left+right)
            else:
                left = nums[i]*i-(p[i-1])
                right = right = (p[-1]-p[i])-(nums[i]*(n-1-i))
                ans.append(left+right)
        return ans
