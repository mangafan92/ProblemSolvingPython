"""
Principe:
    - on sait que le digit en 10**k dans a n'influera pas sur les digits en 10**i avec i < k dans a**2
    - on va donc construire récursivement un nombre qui vérifie la propriété en s'assurant au fur et à mesure que les derniers digits de son carré sont corrects
"""


def getDigit(n: int, digit: int) -> int:
    return (n // 10 ** digit) % 10


def isCorrect(n: int, limit: int = 20) -> bool:
    if n >= 10 ** 19:
        return False
    else:
        for k in range(limit // 2):
            if not getDigit(n, 2 * k) == (10 - k) % 10:
                return False
        return True


def numbers() -> list:
    def numbersRec(n: int, digitToAdd: int) -> list:
        if isCorrect(n ** 2):
            return [n]
        else:
            output = []
            for k in range(10):
                m = n + k * 10 ** digitToAdd
                if isCorrect(m ** 2, digitToAdd + 1):
                    output += numbersRec(m, digitToAdd + 1)
            return output

    return numbersRec(0, 0)


def solve() -> int:
    return numbers()[0]


if __name__ == '__main__':
    print(solve())
