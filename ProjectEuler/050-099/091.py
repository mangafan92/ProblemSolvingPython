import itertools

import time

start = time.time()

def isRightTriangle(points):
    vectors = [
        points[0],
        points[1],
        (points[1][0] - points[0][0], points[1][1] - points[0][1])
    ]

    if (0, 0) in vectors:
        return False

    squaredModule = lambda vector: vector[0]**2 + vector[1]**2
    squaredModules = list(map(squaredModule, vectors))

    pythagore = lambda module: module == sum(squaredModules) - module
    pythagoreResults = list(map(pythagore, squaredModules))

    return True in pythagoreResults

limit = 50
triangles = 0

for x1, x2, y1, y2 in itertools.product(range(limit+1), repeat=4):
    if isRightTriangle([(x1, y1), (x2, y2)]):
        triangles += 1

print(triangles//2)

print(time.time() - start)