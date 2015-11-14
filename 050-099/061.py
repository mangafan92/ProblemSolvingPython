import itertools


def polygonalNumber(n: int, figure: int) -> int:
    functions = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n ** 2,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2)
    }
    return functions[figure](n)


def polygonalNumbersWithNDigits(figure: int, digits: int) -> list:
    numbers = list()
    i = 0

    while polygonalNumber(i, figure) <= 10 ** (digits - 1):
        i += 1

    while polygonalNumber(i, figure) < 10 ** digits:
        numbers.append(polygonalNumber(i, figure))
        i += 1
    return numbers


def begEndPolygonalNumbersWithNDigits(figure: int, digits: int) -> (dict, dict):
    numbers = polygonalNumbersWithNDigits(figure, digits)
    beg = [str(n)[:digits // 2] for n in numbers]
    end = [str(n)[digits // 2:] for n in numbers]
    return beg, end


def begsEnds(minfigure: int, maxfigure: int, digits: int) -> (dict, dict):
    begs, ends = dict(), dict()
    for figure in range(minfigure, maxfigure + 1):
        beg, end = begEndPolygonalNumbersWithNDigits(figure, digits)
        begs[figure] = beg
        ends[figure] = end
    return begs, ends


def possibleOrders(minfigure: int, maxfigure: int) -> list:
    return [[maxfigure] + list(permutation) for permutation in itertools.permutations(range(minfigure, maxfigure))]


def calculateSolutionNumbers(order: list, solution: list, begs: dict, ends: dict) -> list:
    numbers = list()
    for i in range(len(order)):
        numbers.append(int(begs[order[i]][solution[i]] + ends[order[i]][solution[i]]))
    return numbers


def testOrder(order: list, begs: dict, ends: dict) -> list:
    def testOrderRec(partialSet: list, i: int) -> list:
        if i == len(order):
            if begs[order[0]][partialSet[0]] == ends[order[-1]][partialSet[-1]]:
                return [partialSet]
            else:
                return []
        elif i == 0:
            output = []
            for j in range(len(begs[order[0]])):
                output += testOrderRec([j], i + 1)
            return output
        else:
            output = []
            for j in range(len(begs[order[i]])):
                if begs[order[i]][j] == ends[order[i - 1]][partialSet[i - 1]]:
                    output += testOrderRec(partialSet + [j], i + 1)
            return output

    return [calculateSolutionNumbers(order, solution, begs, ends) for solution in testOrderRec([], 0)]


def solve(minfig: int = 3, maxfig: int = 8, digits: int = 4) -> int:
    begs, ends = begsEnds(minfig, maxfig, digits)
    orders = possibleOrders(minfig, maxfig)
    sets = [testOrder(order, begs, ends) for order in orders]
    sets = [s for s in sets if s]
    return sum(sets[0][0])


if __name__ == '__main__':
    print(solve())
