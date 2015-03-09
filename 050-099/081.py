with open("./data/081_matrix.txt", "r") as file:
    content = file.read()

def minimalPathSum(matrix):
    width = len(matrix[0])
    height = len(matrix)
    minimal = [[0]* width for k in range(height)]

    def minimalPathSumRecur(x, y):
        if minimal[x][y] != 0:
            return minimal[x][y]
        else:
            if (x+1, y+1) == (height, width):
                minimal[x][y] = matrix[x][y]
            elif x+1 == width:
                minimal[x][y] = matrix[x][y] + minimalPathSumRecur(x, y+1)
            elif y+1 == height:
                minimal[x][y] = matrix[x][y] + minimalPathSumRecur(x+1, y)
            else:
                minimal[x][y] = matrix[x][y] + min(minimalPathSumRecur(x+1, y), minimalPathSumRecur(x, y+1))
            return minimal[x][y]

    return minimalPathSumRecur(0, 0)

def contentToMatrix(content):
    content = content.splitlines()
    content = list(map(lambda x: x.split(","), content))
    lineToInt = lambda line: list(map(int, line))
    content = list(map(lineToInt, content))
    return content

def solveProblem(content=content):
    return minimalPathSum(contentToMatrix(content))

if __name__ == '__main__':
    print(solveProblem())