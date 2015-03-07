def collatz(n, collatzResults):
    try:
        return collatzResults[n]
    except:
        if n == 1:
            output = 1
        elif n%2 == 0:
            output = 1 + collatz(n//2, collatzResults)
        else:
            output = 1 + collatz(3*n+1, collatzResults)
        collatzResults[n] = output
        return output

def solveProblem(limit=10**6):
    collatzResults = dict()
    longest = 0
    start = 0
    for k in range(1, limit):
        collatzLength = collatz(k, collatzResults)
        if collatzLength > longest:
            longest = collatzLength
            start = k
    return start

if __name__ == '__main__':
    print(solveProblem())