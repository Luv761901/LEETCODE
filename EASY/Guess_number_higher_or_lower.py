class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while(l <= r):
            mid = l+(r-l)//2
            s = guess(mid)
            if s == 1:
                l = mid+1
            elif s == 0:
                return mid
            else:
                r = mid-1
