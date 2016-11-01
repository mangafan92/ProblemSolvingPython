import functools


@functools.lru_cache(maxsize=None)
def collatz(n):
    if n == 1:
        output = 1
    elif n % 2 == 0:
        output = 1 + collatz(n // 2)
    else:
        output = 1 + collatz(3 * n + 1)
    return output


def solveProblem(limit=10 ** 6):
    collatzLengths = {i: collatz(i) for i in range(1, limit + 1)}
    return max(collatzLengths, key=lambda i: (collatzLengths[i], -i))


if __name__ == '__main__':
    print(solveProblem())
