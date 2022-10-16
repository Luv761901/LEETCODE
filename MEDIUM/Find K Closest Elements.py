class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == k:
            return arr
        l, r = 0, len(arr) - k
        mid = 0
        while l < r:

            mid = (l + r) // 2
            print(l, mid, r)

            if (x - arr[mid]) > (arr[mid + k] - x):
                l = mid + 1

            else:
                r = mid
        return arr[l: l + k]
