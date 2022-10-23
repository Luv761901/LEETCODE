class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            binary = bin(i)[2:]
            c = binary.count('1')
            flag = 0
            if c == 1:
                flag = 1
            else:
                for i in range(2, c):
                    if c % i == 0:
                        flag = 1
                        break
                if flag == 0:
                    count += 1

        return count
