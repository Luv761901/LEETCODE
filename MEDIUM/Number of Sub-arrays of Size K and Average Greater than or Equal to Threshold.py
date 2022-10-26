class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ws = 0
        c = 0
        wsum = 0
        for we in range(len(arr)):
            wsum += arr[we]
            if we >= k-1:
                if (wsum//k) >= threshold:
                    c += 1
                wsum -= arr[ws]
                ws += 1
        return c
