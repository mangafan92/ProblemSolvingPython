"""
    Principe:
    - Si x^n possède n chiffres, on peut déjà en déduire plusieurs choses:
        - x < 10 puisque 10**n possède n+1 chiffres (un 1 suivi de n zéros)
        - 9^n s'écrit avec plus de n chiffres (au sens large), sinon x^n possède exactement n chiffres est impossible
        - n >= 1 puisqu'aucun nombre ne s'écrit avec 0 chiffres
"""


def solveProblem():
    result = 0
    n = 1
    while len(str(9**n)) >= n:
        for k in range(1, 10):
            if len(str(k**n)) == n:
                result += 1
        n += 1

    return result

if __name__ == '__main__':
    print(solveProblem())