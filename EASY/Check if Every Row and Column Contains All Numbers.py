class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        x = []
        for i in range(1, len(matrix)+1):
            x.append(i)
        print(x)
        for i in range(len(matrix)):
            if sorted(matrix[i]) != x:
                return False
        a = len(matrix)
        for i in range(a):
            t = []
            for j in range(a):
                t.append(matrix[j][i])
            t.sort()
            if t != x:
                return False
        return True
