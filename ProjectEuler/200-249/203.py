from functools import reduce
from operator import add

from modules.primeDecomposition import PrimeDecomposition

def isSquareFree(n):
    for value in n.values():
        if value > 1:
            return False
    return True

def solveProblem(numberOfRows=51):
    generateRow = lambda row: [PrimeDecomposition.pascalCoefficient(k, row) for k in range(0, row+1)]
    generateRows = lambda rows: [generateRow(k) for k in range(0, rows)]

    rows = generateRows(numberOfRows)
    rows = reduce(add, rows)

    rows = list(filter(isSquareFree, rows))
    rows = list(map(PrimeDecomposition.value, rows))
    rows = list(set(rows))

    return sum(rows)

if __name__ == '__main__':
    print(solveProblem())