content = open("./data/089_roman.txt", "r").read()

romanCharValues = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def evaluateRomanNumeral(s: str) -> int:
    value = 0
    for k in range(len(s)):
        if k + 1 < len(s) and romanCharValues[s[k + 1]] > romanCharValues[s[k]]:
            value -= romanCharValues[s[k]]
        else:
            value += romanCharValues[s[k]]
    return value


def minimumForm(n: int) -> str:
    s = ""
    while n >= 1000:
        n -= 1000
        s = s + "M"

    if n >= 900:
        n -= 900
        s = s + "CM"

    if 500 > n >= 400:
        n -= 400
        s = s + "CD"

    while n >= 500:
        n -= 500
        s = s + "D"

    while n >= 100:
        n -= 100
        s = s + "C"

    if n >= 90:
        n -= 90
        s = s + "XC"

    while n >= 50:
        n -= 50
        s = s + "L"

    if 50 > n >= 40:
        n -= 40
        s = s + "XL"

    while n >= 10:
        n -= 10
        s = s + "X"

    if n == 9:
        n -= 9
        s = s + "IX"

    while n >= 5:
        n -= 5
        s = s + "V"

    if n == 4:
        n -= 4
        s = s + "IV"

    while n > 0:
        n -= 1
        s = s + "I"

    return s


def solve(content: str = content) -> int:
    return sum([len(line) - len(minimumForm(evaluateRomanNumeral(line))) for line in content.splitlines()])


if __name__ == '__main__':
    print(solve())
