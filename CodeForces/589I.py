import collections


def main():
    n, k = list(map(int, input().split()))
    mean = n // k
    colors = list(map(int, input().split()))
    counter = dict(collections.Counter(colors))

    for i in range(1, k + 1):
        if not i in counter:
            counter[i] = 0

    print(sum(abs(counter[i] - mean) for i in counter) // 2)


if __name__ == '__main__':
    main()
