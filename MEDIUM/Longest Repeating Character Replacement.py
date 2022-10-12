class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ws = 0
        maxlen = -math.inf
        maxR = 0
        d = {}
        for we in range(len(s)):
            rightchar = s[we]
            d[rightchar] = d.get(rightchar, 0)+1
            maxR = max(maxR, d[rightchar])
            if (we-ws+1-maxR) > k:
                leftchar = s[ws]
                d[leftchar] = d.get(leftchar)-1
                ws += 1
            maxlen = max(maxlen, we-ws+1)
        return maxlen
