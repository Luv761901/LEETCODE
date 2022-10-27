class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes)-sum(bobSizes))//2
        a = set(aliceSizes)
        b = set(bobSizes)
        for i in a:
            if i-diff in b:
                return [i, i-diff]
