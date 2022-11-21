class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        ans = [0]*len(nums)
        j = 0
        for i in even:
            ans[j] = i
            j += 2
        j = 1
        for i in odd:
            ans[j] = i
            j += 2
        return ans
