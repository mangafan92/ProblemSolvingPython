def solveProblem(limit=1000):
    result = 0

    for k in range (1,limit):
        if k % 3 == 0 or k % 5 == 0:
            result += k

    return result

if __name__ == '__main__':
    print(solveProblem())