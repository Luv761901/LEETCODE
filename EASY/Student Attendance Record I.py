class Solution:
    def checkRecord(self, s: str) -> bool:
        if ('LLL' in s) or (s.count('A') >= 2):
            return False
        else:
            return True
