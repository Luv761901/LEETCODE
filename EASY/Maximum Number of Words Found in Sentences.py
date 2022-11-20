class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1 = 0
        for i in sentences:
            a = i.split()
            s = len(a)
            if s > max1:
                max1 = s
        return max1
