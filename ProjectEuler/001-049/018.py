with open("./data/018_triangle.txt", "r") as file:
    content = file.read()

def maximumPathSum(triangle):
    maximumPathSums = list()
    for line in triangle:
        maximumPathSums.append(list(line))

    for i in range(len(maximumPathSums)):
        for j in range(len(maximumPathSums[i])):
            maximumPathSums[i][j] = 0

    def maximumPathSumRecur(line, column):
        if maximumPathSums[line][column] != 0:
            return maximumPathSums[line][column]
        else:
            if line == len(triangle)-1:
                maximumPathSums[line][column] = triangle[line][column]
            else:
                maximumPathSums[line][column] = triangle[line][column] + max(maximumPathSumRecur(line+1, column), maximumPathSumRecur(line+1, column+1))
            return maximumPathSums[line][column]

    return maximumPathSumRecur(0, 0)

def contentToTriangle(content):
    content = content.splitlines()
    content = list(map(lambda n: n.split(" "), content))
    lineToInt = lambda line: list(map(int, line))
    content = list(map(lineToInt, content))
    return content

def solveProblem(content=content):
    triangle = contentToTriangle(content)
    return maximumPathSum(triangle)

if __name__ == '__main__':
    print(solveProblem())