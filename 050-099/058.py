import random

cornerValues = dict()


def millerRabinTest(n: int, precision: int) -> bool:
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


def cornerValue(corner: int) -> int:
    try:
        return cornerValues[corner]
    except:
        if corner == 0:
            cornerValues[corner] = 1
        else:
            cornerValues[corner] = 2 * ((corner - 1) // 4 + 1) + cornerValue(corner - 1)
        return cornerValues[corner]


def solveProblem(limit: float = 0.10) -> int:
    primescount = 0
    square = 1
    corner = 1

    while corner < 2 or primescount / corner > limit:
        for k in range(4):
            if millerRabinTest(cornerValue(corner), 10):
                primescount += 1
            corner += 1
        square += 2

    return square


if __name__ == '__main__':
    print(solveProblem())
