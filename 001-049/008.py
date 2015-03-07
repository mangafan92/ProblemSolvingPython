from functools import reduce
from operator import mul

with open("./data/008_grid.txt", "r") as file:
    fileContent = file.read()

def solveProblem(digits=fileContent, adjacent=13):
    digits = digits.splitlines()
    digits = "".join(digits)
    digits = list(map(int, digits))

    maximum = 0

    for i in range(0, len(digits)-adjacent):
        maximum = max(maximum, reduce(mul, digits[i:i+adjacent]))

    return maximum

if __name__ == '__main__':
    print(solveProblem())