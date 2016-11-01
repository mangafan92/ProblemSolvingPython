import decimal
decimal.getcontext().prec = 300

def newton(square, precision):
    f = lambda x: x**2 - square

    if int(square)**(1/2)%1 == 0:
        return int(int(square)**(1/2))

    def newtonRec(inf, sup):
        if sup-inf < precision/2:
            return (sup+inf)/2
        else:
            m = (inf+sup)/2

            if f(inf)*f(m) >= 0:
                return newtonRec(m, sup)
            else:
                return newtonRec(inf, m)

    return newtonRec(0, square)

def solveProblem(limit=100):
    roots = [newton(decimal.Decimal(k), 10**-200) for k in range(limit+1)]

    isNotInt = lambda n: not type(n) == int
    roots = list(filter(isNotInt, roots))

    decimals = lambda n: list(str(n*10**200)[0:100])
    roots = list(map(decimals, roots))

    listToInt = lambda l: list(map(int, l))
    roots = list(map(listToInt, roots))

    roots = list(map(sum, roots))

    return sum(roots)

if __name__ == '__main__':
    print(solveProblem())