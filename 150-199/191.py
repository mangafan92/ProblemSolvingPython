import math

symbols = list(range(3))
binomial = lambda k, n: math.factorial(n)/math.factorial(k)/math.factorial(n-k)

def correct(sequence):
    if sequence.count(0) > 1:
        return False

    for k in range(len(sequence)-2):
        if sequence[k:k+3].count(1) == 3:
            return False

    return True

def prizes(days):
    def prizesRecur(beg, rem):
        if correct(beg):
            if rem == 0:
                return 1
            else:
                result = 0
                for symbol in symbols:
                    result += prizesRecur(beg + (symbol,), rem-1)
                return result
        else:
            return 0

    return prizesRecur(tuple(), days)

n = 12
print(3**n, prizes(n))