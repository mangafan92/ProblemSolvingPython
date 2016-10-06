"""
Principe:
    - pas d'autre choix que de déterminer toutes les opérations parenthésées qu'on peut former avec chaque set de 4 digits
    - on représente les opération avec des arbres dont les noeuds sont des fonctions et les feuilles des valeurs

Optimisation:
    - on abuse de yield, pour optimiser l'espace mémoire et avoir un code clair
    - il serait possible d'utiliser la programmation dynamique pour accélérer le programme
"""

from operator import add, sub, mul, floordiv
from itertools import product

operators = (
    add,
    sub,
    mul,
    floordiv,
)


def calculate(tree):
    if len(tree) == 1:
        return tree[0]
    else:
        if tree[0] != floordiv or tree[1] % tree[2] == 0:
            return tree[0](calculate(tree[1]), calculate(tree[2]))
        else:
            raise Exception


def values(trees):
    for tree in trees:
        try:
            yield calculate(tree)
        except:
            pass


def separations(elements):
    for digits in product([0, 1], repeat=len(elements)):
        yield (
            [elements[i] for i in range(len(elements)) if digits[i] == 0],
            [elements[i] for i in range(len(elements)) if digits[i] == 1],
        )


def correct_separations(elements):
    return filter(lambda e: len(e[0]) != 0 and len(e[1]) != 0, separations(elements))


def ascending_until(l):
    if not (l[0] == 1 and l[0] + 1 == l[1]):
        return l[0]
    else:
        i = 0

        while i + 1 < len(l) and l[i] + 1 == l[i + 1]:
            i += 1

        return l[i]


def all_trees(numbers):
    if len(numbers) == 1:
        yield [numbers[0]]
    else:
        for left, right in correct_separations(numbers):
            for operator in operators:
                for left_tree in all_trees(left):
                    for right_tree in all_trees(right):
                        yield [operator, left_tree, right_tree]


def couples():
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    yield (
                        ascending_until(list(sorted(filter(lambda e: e >= 1, set(values(all_trees([a, b, c, d]))))))),
                        [a, b, c, d],
                    )


def solve():
    return "".join(map(str, max(couples())[1]))


print(solve())
