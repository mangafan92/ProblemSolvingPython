with open("./data/081_matrix.txt", "r") as file:
    content = file.read()

def contentToMatrix(content):
    content = content.splitlines()
    content = list(map(lambda x: x.split(","), content))
    lineToInt = lambda line: list(map(int, line))
    content = list(map(lineToInt, content))
    return content

def dijkstra(matrix):
    width = len(matrix[0])
    height = len(matrix)
    costs = [[0]* width for k in range(height)]
    costs[0][0] = matrix[0][0]
    minimums = [(0, 0, costs[0][0])]

    while len(minimums) > 0:
        minimums = list(sorted(minimums, key=lambda n: n[2]))
        addNextCost(minimums, matrix, costs)

    return costs[-1][-1]

def getAdjacentsCases(x, y, costs):
    adjacents = list()
    coordinates = (x+1, y), (x, y+1)

    for coordinate in coordinates:
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
    return dijkstra(contentToMatrix(content))

if __name__ == '__main__':
    print(solveProblem())