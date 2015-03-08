factorials = {k: 1 for k in range(2)}
lengths = {
    169: 3,
    363601: 3,
    1454: 3,
    871: 2,
    45361: 2,
    872: 2,
    45362: 2,
    145: 1
}

def factorial(number):
    try:
        return factorials[number]
    except:
        factorials[number] = number*factorial(number-1)
        return factorials[number]

def nextFactorial(number):
    result = 0
    k = 0
    while number // 10**(k) != 0:
        result += factorial(number%(10**(k+1))//(10**k))
        k += 1
    return result

def sequenceLength(number):
    try:
        return lengths[number]
    except:
        if number != nextFactorial(number):
            lengths[number] = 1 + sequenceLength(nextFactorial(number))
        else:
            lengths[number] = 1
        return lengths[number]

def solveProblem(limit=10**6, length=60):
    result = 0
    for k in range(0, limit):
        if sequenceLength(k) == length:
            result += 1
    return result

if __name__ == '__main__':
    print(solveProblem())