class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        a = []
        for i in range(len(colors)-1):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    a.append(abs(i-j))
        return max(a)
