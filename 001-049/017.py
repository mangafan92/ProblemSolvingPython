writtenNumbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def addPart(number, part):
    if len(number) == 0:
        return part
    else:
        return number + " and " + part

def solveProblem(limit=1000):
    letters= 0
    for k in range(1, limit+1):
        number = str()

        if k // 10**3 > 0:
            number = addPart(number, writtenNumbers[k//10**3] + " thousand")

        k = k % 10**3

        if k // 10**2 > 0:
            number = addPart(number, writtenNumbers[k // 10**2] + " hundred")

        k = k % 10**2

        if k > 0:
            if k < 20:
                number = addPart(number, writtenNumbers[k])
            else:
                number = addPart(number, writtenNumbers[k//10*10])
                if k%10 > 0:
                    number = number + "-" + writtenNumbers[k%10]

        letters += len(number.replace("-", "").replace(" ", ""))

    return letters

if __name__ == '__main__':
    print(solveProblem())
