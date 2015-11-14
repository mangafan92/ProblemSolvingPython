import random


def fastPrimalityTest(n: int, precision: int) -> bool:
    # Miller-Rabin primality test
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        r = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            r += 1

        for i in range(precision):
            if millerRabinSubtest(n, d, r, random.randint(2, n - 1)):
                return False
        return True


def millerRabinSubtest(n: int, d: int, r: int, x: int) -> bool:
    x = pow(x, d, n)
    if x == 1 or x == n - 1:
        return False
    for i in range(r):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True
