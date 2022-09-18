sub = ''
j = 0
while(1):
    try:
        sub += strs[0][j]
    except:
        break
    for i in range(1, len(strs)):
        T = strs[i]
        try:
            if T[j] == sub[j]:
                continue
            else:
                sub = sub[:-1]
                break
        except:
            sub = sub[:-1]
            break
    j += 1
return sub
