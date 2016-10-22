if __name__ == '__main__':
    n = int(input())

    ranks = dict()

    for k in range(n):
        ranks[input()] = k

    for name in reversed(sorted(ranks, key= lambda key: ranks[key])):
        print(name)
