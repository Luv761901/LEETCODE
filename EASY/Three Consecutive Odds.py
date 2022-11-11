class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        for i in arr:
            if i % 2 != 0:
                c += 1
            else:
                c = 0
            if c == 3:
                return True

        return False
