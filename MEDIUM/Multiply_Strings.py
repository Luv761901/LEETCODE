def calc(num):
    ans = 0
    for i in num:
        ans = ans*10+ord(i)-ord('0')
    return ans


return str(calc(num1)*calc(num2))
