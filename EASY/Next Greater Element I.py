class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        ans = [0]*len(nums2)
        for i in range(len(nums2)-1, -1, -1):
            curr = nums2[i]
            while len(stack) != 0 and stack[-1] <= curr:
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(curr)
        for i in range(len(nums2)):
            d[nums2[i]] = ans[i]
        print(d)
        res = []
        for i in nums1:
            res.append(d[i])
        return res
