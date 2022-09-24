s = math.trunc(dividend/divisor)
x = (2**31)-1
y = (-2**31)
if s > x:
    return x
elif s < y:
    return y
else:
    return s
