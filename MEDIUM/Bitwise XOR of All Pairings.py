class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if (n % 2 != 0 and m % 2 == 0):
            p1 = nums2[0]
            for i in range(1, m):
                p1 ^= nums2[i]
            return p1
        elif (n % 2 == 0 and m % 2 != 0):
            p1 = nums1[0]
            for i in range(1, n):
                p1 ^= nums1[i]
            return p1
        elif (n % 2 == 0 and m % 2 == 0):
            return 0
        else:
            p1 = nums2[0]
            for i in range(1, m):
                p1 ^= nums2[i]
            p2 = nums1[0]
            for i in range(1, n):
                p2 ^= nums1[i]
            return p1 ^ p2
