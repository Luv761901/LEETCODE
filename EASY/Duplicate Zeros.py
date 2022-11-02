class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        a=[]
        for i  in range(len(arr)):
            if arr[i]==0:
                a.append(0)
                a.append(0)
            else:
                a.append(arr[i])
        print(a)
        for i  in range(len(a)-1,-1,-1):
            if len(a)==n:
                break
            a.pop()
        for i in range(len(a)):
            arr[i]=a[i]
            