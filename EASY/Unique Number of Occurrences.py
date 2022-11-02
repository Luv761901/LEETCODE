class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        flag = 0
        s = d.values()
        print(s)
        if len(set(s)) == len(s):
            return True
        return False
