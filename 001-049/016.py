def solveProblem(power=1000):
    number = 2**power
    number = list(str(number))
    number = list(map(int, number))
    return sum(number)

if __name__ == '__main__':
    print(solveProblem())