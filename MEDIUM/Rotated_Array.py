arr = nums[::]
for i in range(len(nums)):
    nums[(i+k) % len(arr)] = arr[i]
