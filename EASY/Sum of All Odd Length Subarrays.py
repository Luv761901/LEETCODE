class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        c = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                x = arr[i:j]
                if len(x) % 2 != 0:
                    c += sum(x)
        return c
