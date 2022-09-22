if n == 1:
    return n
else:
    A = [1]
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
        A.append(c)
    A.append(A[-1]+A[-2])
    return A[-1]
