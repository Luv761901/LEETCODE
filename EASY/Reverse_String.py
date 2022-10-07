p = len(s)
for i in range(p//2):
    temp = s[i]
    s[i] = s[p-i-1]
    s[p-i-1] = temp
