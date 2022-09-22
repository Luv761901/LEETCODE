j, k = 0, 0
sum1, sum2 = 0, 0
for i in reversed(a):
    if(i == '0'):
        j += 1
        continue
    else:
        sum1 += 2**j
        j += 1
for i in reversed(b):
    if(i == '0'):
        k += 1
        continue
    else:
        sum2 += 2**k
        k += 1
tot = sum1+sum2
return bin(tot).replace("0b", "")
