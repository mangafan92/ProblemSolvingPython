def startrecur(length):
    numbers = list()
    for k in range(0, 10):
        increasing(str(k), length-1, numbers)
        decreasing(str(k), length-1, numbers)
    return numbers

def increasing(number, length, numbers):
    if length > 0:
        for k in range(int(number)%10, 10):
            increasing(number + str(k), length-1, numbers)
    else:
        if not int(number) in numbers:
            numbers.append(int(number))

def decreasing(number, length, numbers):
    if length > 0:
        if int(number) == 0:
            for k in range(0, 10):
                decreasing(number + str(k), length-1, numbers)
        else:
            for k in range(0, int(number)%10+1):
                decreasing(number + str(k), length-1, numbers)
    else:
        if not int(number) in numbers:
            numbers.append(int(number))

if __name__ == '__main__':
    numbers = startrecur(6)
    numbers.sort()
    print(len(numbers))
    print(numbers)