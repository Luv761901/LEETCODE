class Solution:
    def canPlaceFlowers(self, s: List[int], n: int) -> bool:
        if n == 0:
            return True
        s = [0]+s+[0]
        c = 0
        for i in range(1, len(s)-1):
            if s[i] != 1 and s[i-1] != 1 and s[i+1] != 1:
                c += 1
                s[i] = 1
        if c >= n:
            return True
        return False
