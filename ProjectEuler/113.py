def increasing(length):
    numbers = [ [1]*10 ]

    for k in range(length-1):
        numbers.append([0]*10 )

    for k in range(length-1):
        for i in range(10):
            for j in range(i, 10):
                numbers[k+1][j] += numbers[k][i]

    return sum(numbers[-1])

def decreasing(length):
    output = 0

    for j in range(1, length+1):
        numbers = [ [0] + [1]*9 ]

        for k in range(j-1):
            numbers.append([0]*10 )

        for k in range(j-1):
            for i in range(10):
                for j in range(0, i+1):
                    numbers[k+1][j] += numbers[k][i]
            # print(k, numbers)

        output += sum(numbers[-1])

    return output

if __name__ == '__main__':
    length = 100
    # On enlève les nombres qui sont croissants et décroissants, il y en a 9*length, ainsi que 0
    print(increasing(length) + decreasing(length) - 9*length - 1)