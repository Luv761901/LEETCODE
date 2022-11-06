class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        a = len(grid)
        b = len(grid[0])
        for i in range(a):
            for j in range(b):
                if grid[i][j] < 0:
                    c += 1
        return c
