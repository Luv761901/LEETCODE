class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        d = []
        arr.sort()
        for i in range(len(arr)-1):
            d.append(arr[i+1]-arr[i])
        if len(set(d)) == 1:
            return True
        else:
            return False
