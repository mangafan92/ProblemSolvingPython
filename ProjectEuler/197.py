"""
Principe:
    - la suite u_n + u_(n+1) converge très vite, il suffit de s'arrêter quand les décimales qui nous intéressent ne bougent plus
"""

from math import floor


def f(x):
    return floor(2 ** (30.403243784 - x ** 2)) * 10 ** -9


def solve():
    u0 = -1
    u1 = f(u0)
    u2 = f(u1)

    while abs(u2 - u0) > 10 ** -12:
        u0, u1, u2 = u1, u2, f(u2)

    return round(u1 + u2, 9)


if __name__ == '__main__':
    print(solve())
