class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        Q = []
        Q.append(start)
        while(len(Q) > 0):
            i = Q.pop(0)
            if arr[i] == 0:  # if Target
                return True
            if arr[i] < 0:  # if Visited
                continue
            if i-arr[i] >= 0:
                Q.append(i-arr[i])
            if i+arr[i] < len(arr):
                Q.append(i+arr[i])
            arr[i] = -arr[i]  # here defined visited
        return False
