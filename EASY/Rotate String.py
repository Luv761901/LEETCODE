class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        goal=list(goal)
        b=[0]*len(s)
        k=len(s)
        while(k!=0):
            for i in range(len(s)):
                b[(i+k)%len(s)]=s[i]
            k-=1
            if b==goal:
                return True
        return False    
  