class Solution:
    def findRadius(self, houses: List[int], arr: List[int]) -> int:
        arr.sort()
        def search(num):
            i=0
            j=len(arr)-1
            m=10**10
            while(i<=j):
                mid=(i+j)//2
                m=min(m,abs(arr[mid]-num))
                if m==0:
                    break
                if arr[mid]>num:
                    j=mid-1
                else:
                    i=mid+1
            return m
        ans=0
        for i in houses:
            ans=max(ans,search(i))
        return ans
        
                    
                