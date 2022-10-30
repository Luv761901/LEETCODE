class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        s = len(encoded)+1
        per = 0
        for i in range(s+1):
            per = per ^ i
        first = 0
        for i in range(len(encoded)):
            if i % 2 != 0:
                per = per ^ encoded[i]
        first = per
        ans = [first]
        for i in encoded:
            first = first ^ i
            ans.append(first)
        return ans
