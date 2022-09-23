nums.sort()
n = len(nums)
target = 0
ans = set()
for i in range(n-2):
    l = i+1
    r = n-1
    while l < r:
    Sum = nums[i]
    Sum += nums[l]
    Sum += nums[r]
    if Sum == target:
        ans.add((nums[i], nums[l], nums[r]))
        l += 1
        r -= 1
    elif Sum > target:
        r -= 1
    else:
        l += 1

return ans
