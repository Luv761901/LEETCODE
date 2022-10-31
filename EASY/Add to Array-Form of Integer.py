class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        a=[]
        for i in num:
            s+=str(i)
        p=str(int(s)+k)
        for i in p:
            a.append(i)
        return a    