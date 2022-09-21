last = None
for i in range(len(nums)):
    if last != None and last == nums[i]:
        nums[i] = '_'
    else:
        if(nums[i] == val):
            nums[i] = '_'
        last = nums[i]
while('_' in nums):
    nums.remove('_')
return len(nums)
