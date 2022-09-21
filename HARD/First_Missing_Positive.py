nums = set(nums)
i = 1
while(True):
    try:
        nums.remove(i)
        i += 1
    except:
        return i
