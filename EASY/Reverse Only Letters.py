class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        text = ""
        for i in s:
            if i.isalpha():
                text += i
        text = list(text)
        word = ""
        for i in s:
            if i.isalpha():
                word += text.pop()
            else:
                word += i
        return word
