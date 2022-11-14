class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        a, b = len(word1), len(word2)
        if a == b:
            for i in range(a):
                ans = ans+word1[i]+word2[i]
        elif a < b:
            for i in range(a):
                ans = ans+word1[i]+word2[i]
            ans = ans+word2[a:]
        else:
            for i in range(b):
                ans = ans+word1[i]+word2[i]
            ans = ans+word1[b:]
        return ans
