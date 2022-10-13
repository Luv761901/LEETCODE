class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        s = 4
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                check = 0
                if grid[i][j] == 0:
                    continue
                if i > 0 and grid[i-1][j] == 1:
                    check += 1
                if i < len(grid)-1 and grid[i+1][j] == 1:
                    check += 1

                if j > 0 and grid[i][j-1] == 1:
                    check += 1

                if j < len(grid[0])-1 and grid[i][j+1] == 1:
                    check += 1

                ans += s-check

        return ans
