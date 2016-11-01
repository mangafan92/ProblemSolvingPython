import copy


def permutations(elements: list):
    if elements:
        for e in sorted(elements):
            elementsCopy = copy.copy(elements)
            elementsCopy.remove(e)
            for permutation in permutations(elementsCopy):
                yield [e] + permutation
    else:
        yield []


def solve() -> str:
    for k, permutation in enumerate(permutations(list(map(str, range(0, 10))))):
        if k == 10 ** 6 - 1:
            return "".join(permutation)


if __name__ == '__main__':
    print(solve())
