def startingPoint(room):
    for i, _ in enumerate(room):
        for j, e in enumerate(room[i]):
            if e not in (0, 1):
                return (i, j), directionConversion(e)


def charConversion(char):
    if char == ".":
        return 0
    elif char == "*":
        return 1
    else:
        return char


def directionConversion(direction):
    return ["U", "R", "D", "L"].index(direction)


def rotate(direction):
    return (direction + 1) % 4


def front(square, direction):
    delta = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    return tuple(square[i] + delta[direction][i] for i in range(len(square)))


def collision(front_square, room, size):
    if front_square[0] < 0 or front_square[1] < 0 or front_square[0] >= size[0] or front_square[1] >= size[1]:
        return True
    else:
        return room[front_square[0]][front_square[1]] == 1


def nextSquare(square, direction, room, size):
    if collision(front(square, direction), room, size):
        return square, rotate(direction)
    else:
        return front(square, direction), direction


def main():
    h, w = tuple(map(int, input().split()))
    room = [list(map(charConversion, input())) for _ in range(h)]
    (i, j), direction = startingPoint(room)
    room[i][j] = 0

    squares = {((i, j), direction)}

    while nextSquare((i, j), direction, room, (h, w)) not in squares:
        (i, j), direction = nextSquare((i, j), direction, room, (h, w))
        squares.add(((i, j), direction))

    print(len(list(set((i, j) for (i, j), _ in squares))))


if __name__ == '__main__':
    main()
