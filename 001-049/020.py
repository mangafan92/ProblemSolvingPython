def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def solveProblem(number=100):
    number = factorial(number)
    number = list(str(number))
    number = map(int, number)
    return sum(number)

if __name__ == '__main__':
    print(solveProblem())