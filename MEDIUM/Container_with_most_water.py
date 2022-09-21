start = 0
end = len(height)-1
m = 0
while(start < end):
    x = height[start]
    y = height[end]
    mi = min(x, y)
    m = max(m, mi*(end-start))
    if x < y:
        start += 1
    else:
        end -= 1
return m
