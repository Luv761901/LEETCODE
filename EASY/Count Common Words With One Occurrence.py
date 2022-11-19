class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c = 0
        for i in words2:
            if i in words1 and words1.count(i) == 1 and words2.count(i) == 1:
                c += 1
        return c
