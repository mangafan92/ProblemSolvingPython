import math

precision = 3000

def decimalAppriximation(denominator, precision):
    n = 10**(precision+1) // denominator
    n //= 10
    return n

def getDigits(number, beg, end):
    number %= 10**end
    number //= 10**beg
    return number

def period(n):
    length = int(math.log10(n))
    for k in range(1, length):
        if getDigits(n, k, 2*k) == getDigits(n, 2*k, 3*k):
            return k

    return 0

periods = [0]

for k in range(1, 1000):
    periods.append(period(decimalAppriximation(k, precision)))

print(periods.index(max(periods)))

