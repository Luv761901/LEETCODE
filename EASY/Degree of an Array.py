class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        A = [0]*(max(nums)+1)
        for i in nums:
            A[i] += 1
        d = max(A)
        Deg = []
        for i in range(len(A)):
            if A[i] == d:
                Deg.append(i)
        Ans = []
        for num in Deg:
            i = 0
            j = len(nums)-1
            while(i <= j):
                if nums[i] != num:
                    i += 1
                if nums[j] != num:
                    j -= 1
                if nums[i] == num and nums[j] == num:
                    break
            Ans.append(j-i+1)
        return min(Ans)
