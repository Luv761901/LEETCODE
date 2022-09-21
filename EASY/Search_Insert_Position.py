for i in range(len(nums)):
    if(nums[i] == target):
        p = nums.index(nums[i])
        return p
for i in nums:
    if(target+1 == i):
        p = nums.index(i)
        return p
    elif(target-1 == i):
        p = nums.index(i)+1
        return p
    elif(nums[-1] < target):
        return len(nums)
return 0
