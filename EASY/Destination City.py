class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for i in paths:
            d[i[0]] = d.get(i[0], 0) + 1
            d[i[1]] = d.get(i[1], 0)
        for i in d:
            if d[i] == 0:
                return i
