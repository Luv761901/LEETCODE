class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        min_heap = []
        d = (dict(Counter(nums)))
        for f, n in d.items():
            heappush(min_heap, (n, -f))
        ans = []
        while min_heap:
            x, y = heappop(min_heap)
            while(x != 0):
                ans.append(-y)

                x -= 1
        return ans
