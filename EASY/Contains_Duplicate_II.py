class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = []
        for i in range(len(nums)):
            a.append([nums[i], i])
        a.sort()
        for i in range(len(a)-1):
            j = i+1
            while j < len(a) and abs(a[i][0] == a[j][0]):
                if abs(a[i][1]-a[j][1]) <= k:
                    return True
                j += 1
        return False
