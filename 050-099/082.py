with open("./data/082_matrix.txt", "r") as file:
    content = file.read()

def contentToMatrix(content):
    content = content.splitlines()
    content = list(map(lambda x: x.split(","), content))
    lineToInt = lambda line: list(map(int, line))
    content = list(map(lineToInt, content))
    return content

def dijkstra(matrix, x):
    width = len(matrix[0])
    height = len(matrix)
    costs = [[0]* width for k in range(height)]
    costs[x][0] = matrix[x][0]
    minimums = [(x, 0, costs[x][0])]

    while len(minimums) > 0:
        minimums = list(sorted(minimums, key=lambda n: n[2]))
        addNextCost(minimums, matrix, costs)

    return min(map(lambda line: line[-1], costs))

def getAdjacentsCases(x, y, costs):
    adjacents = list()
    coordinates = (x+1, y), (x, y+1), (x-1, y)

    for coordinate in coordinates:
        if min(coordinate) >= 0:
            try:
                adjacents.append((coordinate[0], coordinate[1], costs[coordinate[0]][coordinate[1]]))
            except:
                pass

    return adjacents

def addNextCost(minimums, matrix, costs):
    minimum = minimums[0]

    for adjacent in getAdjacentsCases(minimum[0], minimum[1], costs):
        if adjacent[2] == 0:
            costs[adjacent[0]][adjacent[1]] = costs[minimum[0]][minimum[1]] + matrix[adjacent[0]][adjacent[1]]
            minimums.append((adjacent[0], adjacent[1], costs[adjacent[0]][adjacent[1]]))

    minimums.remove(minimum)

def solveProblem(content=content):
    matrix = contentToMatrix(content)
    return min([dijkstra(matrix, k) for k in range(80)])

if __name__ == '__main__':
    print(solveProblem())