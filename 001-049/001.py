def solveProblem(limit=1000):
    return sum([k for k in range(limit + 1) if k % 5 == 0 or k % 3 == 0])

if __name__ == '__main__':
    print(solveProblem())