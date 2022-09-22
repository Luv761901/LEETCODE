s = ""
ans = []
for i in digits:
    s += str(i)
x = str(int(s)+1)
for i in x:
    ans.append(int(i))
return ans
