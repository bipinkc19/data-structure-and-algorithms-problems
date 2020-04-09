"""Write a program to find the exponential of numbers pow(a, b)
"""

def power(a, b, flag=None):
    negative = True if b < 0 else False
    b = abs(b)

    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b == 2:
        return a * a
    else:
        if b % 2 == 0:
            res = power(a, b//2, flag) * power(a, b//2, flag)
        else:
            res = power(a, (b-1)//2, flag) * power(a, (b-1)//2, flag) * a

    if negative:
        return 1 / res
    else:
        return res

print(power(2, -4))
print(power(-2, 3))
