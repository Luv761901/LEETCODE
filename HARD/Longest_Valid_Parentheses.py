c = 0
lst = [-1]
for i in range(len(s)):
    if s[i] == '(':
        lst.append(i)
    else:
        lst.pop()
        if lst == []:
            lst.append(i)
        else:
            c = max(c, i-lst[-1])
return c
