class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        col = n-1
        for i in range(m):
            l, r = 0, col
            while l <= r:
                mid = (l+r) >> 1
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid-1
                else:
                    l = mid+1
        return False
