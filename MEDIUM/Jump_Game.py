l = len(nums)-1
for i in range(len(nums)-1, -1, -1):
    if i+nums[i] >= l:
        l = i
return l == 0
