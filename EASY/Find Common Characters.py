class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = list(words[0])
        for i in words:
            x = []
            for c in i:
                if c in s:
                    x.append(c)
                    s.remove(c)
            s = x
        return s
