class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        a = len(nums)
        b = 2**a
        for i in range(b):
            x = bin(i)[2:]
            dif = '0'*(a-len(x))+x
            if dif not in nums:
                return dif
