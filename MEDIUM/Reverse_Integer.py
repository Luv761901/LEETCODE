if x > 0:
    s = str(x)
    s = s[::-1]
    p = int(s)
    if p > (2**31-1) or p < ((-2)**31):
        return 0
    else:
        return p
else:
    x = (-1)*x
    s = str(x)
    s = s[::-1]
    p = (-1)*int(s)
    if p > (2**31-1) or p < ((-2)**31):
        return 0
    else:
        return p
