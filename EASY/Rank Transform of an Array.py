class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = []
        d = {}
        arr1 = sorted(set(arr))
        for i in range(len(arr1)):
            if arr1[i] not in d:
                d[arr1[i]] = i+1

        for i in range(len(arr)):
            res.append(d.get(arr[i]))
        return res
