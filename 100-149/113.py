# TODO

def startrecur(length):
    numbers = [0]
    for k in range(0, 10):
        increasing(k, length-1, numbers)

    for k in range(1, 10):
        decreasing(k, length - 1, False, numbers)
    decreasing(0, length - 1, True, numbers)

    return numbers

def increasing(number, length, numbers):
    if length > 0:
        for k in range(number, 10):
            increasing(k, length-1, numbers)
    else:
        numbers[0] += 1

def decreasing(number, length, start, numbers):
    if length > 0:
        if start:
            decreasing(0, length - 1, True, numbers)
            for k in range(1, 10):
                decreasing(k, length - 1, False, numbers)
        else:
            for k in range(0, number+1):
                decreasing(k, length - 1, False, numbers)
    else:
        numbers[0] += 1

if __name__ == '__main__':
    length = 6
    numbers = startrecur(length)
    numbers.sort()
    # On enlève tous les nombes qui sont croissants et décroissants, ainsi que les 2 fois où 0 apparait
    print(numbers[0] - 9*length - 2)