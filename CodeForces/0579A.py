def binary(n):
    while n > 0:
        yield n % 2
        n //= 2


def main():
    n = int(input())
    print(sum(binary(n)))


if __name__ == '__main__':
    main()
