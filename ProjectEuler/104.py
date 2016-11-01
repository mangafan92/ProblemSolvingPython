import decimal

phi = decimal.Decimal((1+5**(1/2))/2)

lastDigits = {1: 1, 2: 1}

def getLastDigits(n):
    try:
        return lastDigits[n]
    except:
        lastDigits[n] = (getLastDigits(n-1) + getLastDigits(n-2))%10**9
        return lastDigits[n]

def getFirstDigits(n):
    fibonacci = phi**decimal.Decimal(n)/decimal.Decimal(5**(1/2))

    while fibonacci >= 10**9:
        fibonacci /= 10

    return int(fibonacci)

def isPandigital(number):
    number = str(number)
    for digit in map(str, range(1, 10)):
        if not digit in number:
            return False
    return True

def solveProblem():
    n = 3

    while True:
        while not isPandigital(getLastDigits(n)):
            n += 1
        if isPandigital(getFirstDigits(n)):
            return n
        else:
            n += 1

if __name__ == '__main__':
    print(solveProblem())