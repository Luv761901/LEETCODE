class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)
        for i in range(len(encoded)):
            first = first ^ encoded[i]
            ans.append(first)
        return ans
