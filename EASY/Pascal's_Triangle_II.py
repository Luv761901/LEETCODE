class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        for i in range(rowIndex+1):
            x = []
            for j in range(i+1):
                x.append((factorial(i)//(factorial(j)*factorial(i-j))))
            l.append(x)
        return l[rowIndex]
