class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 == [0] and arr2 != [0]:
            return arr2
        elif arr2 == [0] and arr1 != [0]:
            return arr1
        j, k = 0, 0
        s, p = 0, 0
        for i in reversed(arr1):
            if i == 0:
                j += 1
                continue
            else:
                s += (-2)**j
                j += 1
        for i in reversed(arr2):
            if i == 0:
                k += 1
                continue
            else:
                p += (-2)**k
                k += 1
        tot = s+p
        print(tot)
        if tot == 0:
            return [0]
        res = []
        while tot:
            tot, rem = divmod(tot, -2)
            if rem < 0:
                tot += 1
            res.append(abs(rem))
        res.reverse()
        return res
