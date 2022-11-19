class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a = []
        p = s.split()
        for i in p:
            if i.isdigit():
                a.append(int(i))
        print(a)
        flag = True
        for i in range(len(a)-1):
            if a[i] >= a[i+1]:
                flag = False
                return flag
        return flag
