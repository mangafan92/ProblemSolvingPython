from functools import reduce

def greatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(b, a % b)

def smallestCommonMultiple(a, b):
    return a*b // greatestCommonDivisor(a, b)

def solveProblem(minimum=1, maximum=20):
    return reduce(smallestCommonMultiple, range(minimum, maximum+1))

if __name__ == '__main__':
    print(solveProblem())