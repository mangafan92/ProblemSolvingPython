def solveProblem(limit=1000):
    return sum([i**i for i in range(1, limit+1)]) % 10**10

if __name__ == '__main__':
    print(solveProblem())