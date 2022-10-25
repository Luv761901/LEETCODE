class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def validIndex(s,i):
            backspace=0
            while(i>=0):
                if s[i]=='#':
                    backspace+=1
                elif backspace>0:
                    backspace-=1
                else:
                    break
                i-=1
            return i    
        i,j=len(s)-1,len(t)-1
        while(True):
            vI1=validIndex(s,i)
            vI2=validIndex(t,j)
            if vI1<0 and vI2<0:
                return  True
            if vI1<0 or vI2<0:
                return False
            if s[vI1]!=t[vI2]:
                return False
            i=vI1-1
            j=vI2-1