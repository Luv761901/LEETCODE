class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ws = 0
        ans = []
        for we in range(len(nums)):
            if we >= k-1:
                s = we-ws+1
                if s % 2 != 0:
                    x = s//2
                    A = nums[ws:we+1]
                    A.sort()
                    ans.append(A[x])
                    ws += 1
                else:
                    x = s//2
                    y = (s//2)-1
                    A = nums[ws:we+1]
                    A.sort()
                    ans.append((A[x]+A[y])/2)
                    ws += 1
        return ans
