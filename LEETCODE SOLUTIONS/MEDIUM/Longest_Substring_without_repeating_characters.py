S = set()
c = 0
for i in s:
    if i not in S:
        S.add(i)
        c = max(c, len(S))
    else:
        S = S[S.find(i)+1:]+i
return c
