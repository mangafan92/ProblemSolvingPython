def fibonacci(n):
    def fibonacciRecur(a, b, n):
        if n == 0:
            return b
        else:
            return fibonacciRecur(b, a+b, n-1)

    return fibonacciRecur(1, 1, n)

def solveProblem(limit=4*10**6):
    result = 0
    n = 0

    fn = fibonacci(n)

    while fn < limit:
        if fn%2 == 0:
            result += fn
        n += 1
        fn = fibonacci(n)

    return result

if __name__ == '__main__':
    print(solveProblem())