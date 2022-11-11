class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a = arr[-1]
        b = []
        for i in range(1, a+1):
            if i not in arr:
                b.append(i)
        print(b)
        if len(b) == 0:
            return a+k
        elif len(b) >= k:
            return b[k-1]
        else:
            for i in range(1, k-len(b)+1):
                b.append(max(arr)+i)
            return b[-1]
