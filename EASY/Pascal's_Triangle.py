l = []
for i in range(numRows):
    x = []
    for j in range(i+1):
        x.append((factorial(i)//(factorial(j)*factorial(i-j))))
    l.append(x)
return l
