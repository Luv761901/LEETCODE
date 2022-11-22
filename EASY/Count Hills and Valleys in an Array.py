class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        num = 0
        lis = []
        for n in nums:
            if n != num:
                num = n
                lis.append(num)
        count = 0
        for i in range(1, len(lis)-1):
            if lis[i] > lis[i-1] and lis[i] > lis[i+1]:
                count += 1
            elif lis[i] < lis[i-1] and lis[i] < lis[i+1]:
                count += 1
        return count
