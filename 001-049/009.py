def solveProblem(number=1000):
    for a in range(1, number+1):
        for b in range(a+1, number+1):
            if a + b + (a**2 + b**2)**(1/2) == number:
                return int(a*b*(a**2 + b**2)**(1/2))

if __name__ == '__main__':
    print(solveProblem())