ans = min(nums)
S = 0
for i in nums:
    S += i
    ans = max(ans, S)
    if S < 0:
        S = 0
return ans
