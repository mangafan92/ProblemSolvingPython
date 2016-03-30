"""
Principe:
    - pour que l'origine soit dans le triangle, il faut que, pour chaque sommet du triangle, l'origine et ce sommet soient du même côté de la droite définie par les 2 autres sommets du triangle
"""

with open("./data/102_triangles.txt", "r") as file:
    content = file.read()

def contentToTriangles(content):
    content = content.splitlines()
    splitline = lambda line: line.split(",")
    content = list(map(splitline, content))
    lineToInt = lambda line: list(map(int, line))
    content = list(map(lineToInt, content))
    lineToPoints = lambda line: [(line[2*k], line[2*k+1]) for k in range(len(line)//2)]
    content = list(map(lineToPoints, content))
    return content

def containOrigin(triangle):
    for k in range(len(triangle)):
        if not isPointAndOriginAboveLine(triangle, k):
            return False
    return True

def isPointAndOriginAboveLine(triangle, point):
    line = list(triangle)
    line.pop(point)
    point = triangle[point]

    if line[0][0] == line[1][0]:
        return (0 >= line[0][0] and point[0] >= line[0][0]) or (0 <= line[0][0] and point[0] <= line[0][0])
    else:
        a = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
        b = line[0][1] - line[0][0]*a
        return (a*point[0]+b <= point[1] and b <= 0) or (a*point[0]+b >= point[1] and b >= 0)

def solveProblem(content=content):
    return len(list(filter(containOrigin, contentToTriangles(content))))

if __name__ == '__main__':
    print(solveProblem())