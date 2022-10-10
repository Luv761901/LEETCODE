class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        print(letters)
        c = 0
        flag = 0
        for i in letters:
            if letters[i] % 2 == 0:
                c += letters[i]
            else:
                c += letters[i]-1
                flag = 1
        if flag == 1:
            return c+flag
        return c
