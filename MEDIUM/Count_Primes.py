class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return 0
        check=[True for i in range(n+1)]
        check[0]=False
        check[1]=False
        c=0
        for i in range(2,n):
            if check[i]==True:
                c+=1
                for j in range(i**2,n+1,i):
                    check[j]=False
        return c
