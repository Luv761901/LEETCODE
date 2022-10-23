class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a = []
        for i in range(left, right+1):
            flag = 1
            for j in str(i):
                if int(j) == 0:
                    flag = 0
                    break
                elif i % int(j) != 0:
                    flag = 0
            if flag == 1:
                a.append(i)
        return a
