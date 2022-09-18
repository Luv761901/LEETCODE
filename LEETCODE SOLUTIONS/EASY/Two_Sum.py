nums.sort()
l = 0
r = len(nums)-1
while(l < r):
    if nums[l]+nums[r] == target:
        return [l, r]
    elif nums[l]+nums[r] > target:
        r -= 1
    else:
        l += 1
