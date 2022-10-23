class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        d=dict(Counter(nums))
        for i in d:
            if d[i]>1:
                ans.append(i)
                break
        i=1
        while i in d:
            i+=1
        ans.append(i)
        return ans