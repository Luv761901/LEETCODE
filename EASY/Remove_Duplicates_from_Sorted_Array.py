l = None
for i in range(len(nums)):
    if l != None and l == nums[i]:
        nums[i] = '_'
    else:
        l = nums[i]
while('_' in nums):
    nums.remove('_')
return len(nums)
