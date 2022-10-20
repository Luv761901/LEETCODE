class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while(l <= r):

            if l == r:
                return l
            m = (l+r) >> 1
            if l+1 == r:
                if arr[l] > arr[r]:
                    return l
                else:
                    return r
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            else:
                if arr[m] > arr[m+1] and arr[m] < arr[m-1]:
                    r = m-1
                else:
                    l = m+1
