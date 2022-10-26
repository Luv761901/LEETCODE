class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            f = 0
            x = nums[l[i]:r[i]+1]
            x.sort()
            y = x[1]-x[0]

            for j in range(2, len(x)):
                if x[j]-x[j-1] != y:
                    f = -1
                    break
            if f != -1:
                ans.append(True)
            else:
                ans.append(False)
        return ans
