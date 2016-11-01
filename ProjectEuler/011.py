from functools import reduce
from operator import mul

with open("./data/011_grid.txt", "r") as file:
    content = file.read()

def gridOfContent(content):
    content = content.splitlines()
    content = list(map(lambda n: n.split(" "), content))

    lineToInt = lambda line: list(map(int, line))
    content = list(map(lineToInt, content))

    return content

def transpose(grid):
    output = [len(grid[0])*[0] for k in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            output[j][i] = grid[i][j]

    return output

def generateVerticalSymetric(grid):
    output = list(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            output[i][j] = grid[len(grid)-1-i][j]

    return output

def maxLineProduct(grid, adjacent):
    maxProduct = 0
    for line in grid:
        for i in range(0, len(line)-adjacent):
            maxProduct = max(maxProduct, reduce(mul, line[i:i+adjacent]))
    return maxProduct

def maxDiagonalProduct(grid, adjacent):
    maxProduct = 0
    for i in range(len(grid)-adjacent):
        for j in range(len(grid[i])-adjacent):
            diagonal = [grid[i+k][j+k] for k in range(adjacent)]
            maxProduct = max(maxProduct, reduce(mul, diagonal))
    return maxProduct

def solveProblem(content=content, adjacent=4):
    grid = gridOfContent(content)
    transposed = transpose(grid)
    symetric = generateVerticalSymetric(grid)

    maxProducts = (
        maxLineProduct(grid, adjacent),
        maxLineProduct(transposed, adjacent),
        maxDiagonalProduct(grid, adjacent),
        maxDiagonalProduct(symetric, adjacent)
    )

    return max(maxProducts)

if __name__ == '__main__':
    print(solveProblem())