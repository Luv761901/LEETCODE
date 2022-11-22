class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c = 0
        s = len(pref)
        for i in words:
            if i[:s] == pref:
                c += 1
        return c
