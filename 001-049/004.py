import itertools

def isPalindromic(number):
    return str(number) == str(number)[::-1]

def solveProblem(digits=3):
    largest = 0

    for i, j in itertools.product(range(10**(digits-1)-1, 10**digits-1), repeat=2):
        if isPalindromic(i*j):
            largest = max(largest, i*j)

    return largest

if __name__ == '__main__':
    print(solveProblem())