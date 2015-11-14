from modules.fastPrimalityTest import fastPrimalityTest

cornerValues = dict()


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
            if fastPrimalityTest(cornerValue(corner), 10):
                primescount += 1
            corner += 1
        square += 2

    return square


if __name__ == '__main__':
    print(solveProblem())
