class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        p = s[::-1]
        if s == p:
            return True
        else:
            return False
