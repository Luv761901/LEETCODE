class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        m=max(candies)
        for i in candies:
            b=i+extraCandies
            if b>=m:
                a.append(True)
            else:
                a.append(False)
        return a        