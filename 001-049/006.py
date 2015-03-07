def sumOfSquares(n):
    return n*(n+1)*(2*n + 1) // 6

def squareOfSum(n):
    return (n*(n+1)//2)**2

def solveProblem(number=100):
    return squareOfSum(number)-sumOfSquares(number)

if __name__ == '__main__':
    print(solveProblem())