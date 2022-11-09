class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def nser(n):
            stack = []
            ans = [n-1]*n
            for i in range(n-1, -1, -1):
                while(len(stack) != 0 and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                if stack:
                    ans[i] = stack[-1]-1
                stack.append(i)
            return ans

        def nsel(n):
            stack = []
            ans = [0]*n
            for i in range(n):
                while(len(stack) != 0 and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                if stack:
                    ans[i] = stack[-1]+1
                stack.append(i)
            return ans
        ans = heights[0]
        x = nser(len(heights))
        y = nsel(len(heights))
        for i in range(len(heights)):
            m = ((x[i]-y[i]+1)*heights[i])
            if ans < m:
                ans = m
        return ans
