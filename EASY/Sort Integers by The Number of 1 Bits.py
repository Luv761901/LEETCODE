class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        d = {}
        for i in arr:
            x = bin(i)[2:]
            y = x.count('1')
            if d.get(y, -1) == -1:
                d[y] = [i]
            else:
                arr = d[y]
                arr.append(i)
                d[y] = arr
        c = 0
        print(d)
        for i in sorted(d.keys()):
            for j in sorted(d[i]):
                ans.append(j)
        return ans
