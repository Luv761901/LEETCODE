class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i==j or i+j==n-1:
                    s+=mat[i][j]
        return s            