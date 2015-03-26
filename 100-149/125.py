def sumSquares(max):
    return (2*max+1)*(max+1)*max//6

def palindromicNumbers(length):
    beg = list(range(10**(length//2-1), 10**(length//2)))
    beg = list(map(str, beg))
    if length%2 == 0:
        numbers = [int(beg[k] + beg[k][::-1]) for k in range(len(beg))]
        return numbers

    else:
        numbers = list()

        for i in range(len(beg)):
            for j in range(10):
                numbers.append(int(beg[i] + str(j) + beg[i][::-1]))

        return numbers

def generateSums(max):
    sums = set()

    for i in range(max):
        for j in range(i-1):
            sums.add(sumSquares(i) - sumSquares(j))

    return sums

def generatePalindromicNumbers(maxLength):
    numbers = list(range(2, 10))

    for k in range(2, maxLength+1):
        numbers += palindromicNumbers(k)

    return numbers

def solveProblem(maxlength=8):
    sums = generateSums(10**(maxlength//2 + maxlength%2))
    numbers = generatePalindromicNumbers(maxlength)
    numbers = list(filter(lambda n: n in sums, numbers))
    return sum(numbers)

if __name__ == '__main__':
    print(solveProblem())