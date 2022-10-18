class Solution:
    def maximumSwap(self, num: int) -> int:
        l=list(str(num))
        d={}
        for i in range(len(l)):
            d[l[i]]=i
        a=l[:]    
        a.sort(reverse=True)
        for i in range(len(a)):
            if a[i]!=l[i]:
                x=d[a[i]]
                l[i],l[x]=l[x],l[i]
                break
        return int(''.join(l))      