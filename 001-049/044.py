def isPentagonal(x):
    return (1 + (1+24*x)**(1/2))/6 % 1 == 0

def pentagonal(n):
    return n*(3*n-1)//2

def solveProblem():
    i = 0
    while True:
        for j in range(1, i):
            if isPentagonal(pentagonal(i)+pentagonal(j)) and isPentagonal(pentagonal(i)-pentagonal(j)):
                return pentagonal(i)-pentagonal(j)
        i += 1

if __name__ == '__main__':
    print(solveProblem())