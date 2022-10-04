class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def islands(grid, i, j):
            if grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                if (i+1) < len(grid):
                    islands(grid, i+1, j)
                if (i-1) >= 0:
                    islands(grid, i-1, j)
                if (j+1) < len(grid[0]):
                    islands(grid, i, j+1)
                if (j-1) >= 0:
                    islands(grid, i, j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    islands(grid, i, j)
        return count
