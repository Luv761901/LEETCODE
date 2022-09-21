d = {}
print(d)
for i, j in enumerate(nums):
    x = target-j
    if x in d:
        return [d[x], i]
    d[j] = i

# Time Complexity: O(N)
# Space Complexity: O(N)
