def say(n):
    if n == 1:
        return "1"
    a = say(n-1)
    c = 1
    ans = ""
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            c += 1
        else:
            ans += str(c)+a[i]
            c = 1
    if c is not None:
        ans += str(c)+a[-1]
    return ans


ans = say(n)
return ans
