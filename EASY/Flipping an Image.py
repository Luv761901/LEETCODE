class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(image)):
            s=image[i]
            s.reverse()
            for j in range(len(s)):
                if s[j]==0:
                    s[j]=1
                else:
                    s[j]=0
            ans.append(s)        
        return ans   
            