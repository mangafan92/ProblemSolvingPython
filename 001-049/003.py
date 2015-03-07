def solveProblem(number=600851475143):
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            number //= divisor
        else:
            divisor += 1

    return divisor

if __name__ == '__main__':
    print(solveProblem())