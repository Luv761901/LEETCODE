class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = "X"
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "X":
                    matrix[i][j] = 0
                    x, y = 0, 0
                    while(x < len(matrix[0])):
                        if matrix[i][x] != "X":
                            matrix[i][x] = 0
                        x += 1
                    while(y < len(matrix)):
                        if matrix[y][j] != "X":
                            matrix[y][j] = 0
                        y += 1
