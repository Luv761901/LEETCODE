class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r, c1 = [], []
        ans = []
        for i in matrix:
            r.append(min(i))
        for i in range(len(matrix[0])):
            c = []
            for j in range(len(matrix)):
                c.append(matrix[j][i])
            c1.append(max(c))
        for i in r:
            if i in c1:
                ans.append(i)
        return ans
