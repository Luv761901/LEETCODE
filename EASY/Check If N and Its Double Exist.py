class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = 0
        if arr.count(0) > 1:
            return True
        for i in arr:
            if 2*i in arr and i != 0:
                c += 1
                break
        if c == 0:
            return False
        else:
            return True
