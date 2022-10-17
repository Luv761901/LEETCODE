class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = len(candyType)//2
        p = set(candyType)
        x = len(p)
        if s == x:
            return x
        elif x > s:
            return s
        else:
            return x
        print(x)
