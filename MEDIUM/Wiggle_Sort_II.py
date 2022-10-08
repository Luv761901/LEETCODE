class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        a = len(nums)//2
        n1 = nums[:a]
        n2 = nums[a:]
        nums.clear()
        for i in range(len(n1)):
            nums.append(n2[i])
            nums.append(n1[i])
        if len(n2) > len(n1):
            nums.append(n2[-1])
