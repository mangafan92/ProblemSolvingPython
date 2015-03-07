def latticePaths(height, width):
    results = [[0]*(height+1) for i in range(width+1)]

    def latticePathsRecur(x, y):
        if results[x][y] != 0:
            return results[x][y]
        else:
            if x == width or y == height:
                return 1
            else:
                results[x][y] = latticePathsRecur(x+1, y) + latticePathsRecur(x, y+1)
                return results[x][y]

    return latticePathsRecur(0, 0)

def solveProblem(size=20):
    return latticePaths(size, size)

if __name__ == '__main__':
    print(solveProblem())