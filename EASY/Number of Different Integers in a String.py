class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        S=""
        a=[]
        for i in word:
            if i.isnumeric():
                S+=i
            else:
                S+= " "
        print(S)
        S=S.split()
        for i in S:
            a.append(int(i))
        return len(set(a))