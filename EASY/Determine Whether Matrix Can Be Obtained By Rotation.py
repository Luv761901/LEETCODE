class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        def rotate(mat):
            for i in range(len(mat)):
                for j in range(i+1, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            l = 0
            r = len(mat)-1
            while(l < r):
                for k in range(len(mat)):
                    mat[k][l], mat[k][r] = mat[k][r], mat[k][l]
                l += 1
                r -= 1
            return mat

        for i in range(3):
            x = rotate(mat)
            print(x)
            if x == target:
                return True
        return False
