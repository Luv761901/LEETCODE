class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = word.find(ch)
        s1 = ""
        for i in range(len(word)):
            if i == s+1:
                break
            else:
                s1 += word[i]
        s1 = s1[::-1]
        s1 += word[s+1:]
        return s1
