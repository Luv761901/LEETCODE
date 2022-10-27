class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=len(matrix)
        b=len(matrix[0])
        ans=[]
        for i in range(b):
            x=[]
            for  j in range(a):
                x.append(matrix[j][i])
            ans.append(x)    
        return ans