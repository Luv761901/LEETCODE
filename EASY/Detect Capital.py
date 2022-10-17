class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag=0
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper():
                for i in range(1,len(word)):
                    s=ord(word[i])
                    if  s>=97 and s<=122:
                        continue
                    else:
                        flag=-1
                        break
                if flag==0:
                    return  True
                else:
                    return False
        else:
            return False