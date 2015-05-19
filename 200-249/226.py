def distance(x):
    return abs(round(x) - x)


def blancmange(x, precision=200):
    return sum([distance(2 ** n * x) / 2 ** n for n in range(precision)])


def infCircle(x):
    return 1 / 2 - (1 / 16 - (x - 1 / 4) ** 2) ** (1 / 2)


def integrate(function, inf, sup, precision=10000):
    gap = (sup - inf) / precision
    x = [inf + k * gap for k in range(precision + 1)]
    y = [gap * function(x) for x in x]
    return sum(y)


def intersection(function1, function2, start, gap):
    k = 0
    while abs(function1(start + k * gap) - function2(start + k * gap)) > 2 * gap:
        k += 1
    return start + k * gap

def solve():
    intersectionX = intersection(blancmange, infCircle, 0, 10**-5)
    
    blancmangeArea = integrate(blancmange, intersectionX, 0.5, 50000)
    infCircleArea = integrate(infCircle, intersectionX, 0.5, 50000)

    return round(blancmangeArea - infCircleArea, 8)

if __name__ == '__main__':
    print(solve())