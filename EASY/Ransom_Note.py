class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = [0]*26
        for i in ransomNote:
            a[ord(i)-97] += 1
        for i in magazine:
            if a[ord(i)-97] != 0:
                a[ord(i)-97] -= 1
        if sum(a) == 0:
            return True
        else:
            return False
