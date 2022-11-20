class Solution:
    def checkString(self, s: str) -> bool:
        flag = 0
        x = s.find('b')
        if 'b' not in s:
            return True
        for i in range(x+1, len(s)):
            if s[i] == 'a':
                flag = 1
        if flag == 1:
            return False
        else:
            return True
