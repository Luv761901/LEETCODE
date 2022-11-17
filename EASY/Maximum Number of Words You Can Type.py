class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = []
        for i in brokenLetters:
            s.append(i)
        p = text.split()
        x = len(p)
        for i in p:
            for j in i:
                if j in s:
                    x -= 1
                    break
        if x < 0:
            return 0
        return x
