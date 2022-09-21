m = ""
for i in range(len(s)):
    j = k = i
    while(j >= 0 and k < len(s)):
        if s[j] == s[k]:
            sub = s[j:k+1]
            if len(sub) > len(m):
                m = sub
            j -= 1
            k += 1
        else:
            break

    j = i
    k = i+1
    while(j >= 0 and k < len(s)):
        if s[j] == s[k]:
            sub = s[j:k+1]
            if len(sub) > len(m):
                m = sub
            j -= 1
            k += 1

        else:
            break
return m
