def digitsSum(n):
    n = str(n)
    n = list(map(int, n))
    return sum(n)

def powerSum(n):
    numbers = set()

    k = 2
    while len(str(n**k)) <= n:
        if digitsSum(n**k) == n:
            numbers.add(n**k)
        k += 1

    return list(numbers)

def solveProblem(rank=30):
    numbers = list()
    k = 2

    while len(numbers) < rank*3:
        numbers += powerSum(k)
        k += 1

    numbers = list(sorted(numbers))

    return numbers[rank-1]

if __name__ == '__main__':
    print(solveProblem())