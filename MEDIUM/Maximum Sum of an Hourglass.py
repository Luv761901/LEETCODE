class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0
        s = -math.inf
        for i in range(n-2):
            for j in range(m-2):
                x = (grid[i][j]+grid[i][j+1]+grid[i][j+2])+grid[i +
                                                                1][j+1]+(grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])
                if x > s:
                    s = x
        return s
