import itertools

def rectangles(width, height):
    sizes = list(itertools.product(range(1, width+1), range(1, height+1)))
    number = lambda size: (width+1-size[0])*(height+1-size[1])
    numbers = list(map(number, sizes))
    return sum(numbers)

def solveProblem(limit=2*(10**6)):
    areas = list()
    width = 1
    while rectangles(width, 1) <= limit:
        height = 1
        while rectangles(width, height) <= limit:
            height += 1
        areas.append((width*height, rectangles(width, height)))
        if min(width, height) > 1:
            areas.append((width*(height-1), rectangles(width, height-1)))
        width += 1

    areas = list(map(lambda area: (area[0], abs(area[1]-limit)), areas))
    areas = list(sorted(areas, key=lambda area: area[1]))
    return areas[0][0]

if __name__ == '__main__':
    print(solveProblem())