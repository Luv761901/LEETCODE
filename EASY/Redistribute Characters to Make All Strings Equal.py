class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = ''.join(words)
        s1 = set(s)
        for i in s1:
            if s.count(i) % len(words) != 0:
                return False
        return True
