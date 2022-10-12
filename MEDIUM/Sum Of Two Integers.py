class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) > 0:
            carry = (a & b) << 1  # most comes here
            a = a ^ b  # remaining comes here
            b = carry

        if b > 0:
            return a & mask
        return a
