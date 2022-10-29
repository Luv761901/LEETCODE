class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            mid = arr.index(max(arr))
            if mid == arr.index(arr[-1]):
                return False
            elif mid == arr.index(arr[0]):
                return False
            print(mid)
            start_flag = 0
            for i in range(mid-1):
                if arr[i] < arr[i+1]:
                    continue
                else:
                    start_flag = -1
                    break
            if start_flag != 0:
                return False
            else:
                end_flag = 0
                for i in range(mid, len(arr)-1):
                    if arr[i] > arr[i+1]:
                        continue
                    else:
                        end_flag = -1
                        break
                if end_flag != 0:
                    return False
                else:
                    return True
