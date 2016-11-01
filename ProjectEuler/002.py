def fibonacciDyn(limit):
    output = [1, 2]
    while output[-1] <= limit:
        output.append(output[-1] + output[-2])
    return output[:-1]


def solveProblem(limit=4 * 10 ** 6):
    terms = fibonacciDyn(limit)
    isEven = lambda n: n % 2 == 0
    terms = filter(isEven, terms)
    return sum(terms)


if __name__ == '__main__':
    print(solveProblem())