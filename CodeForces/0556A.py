if __name__ == '__main__':
    n = int(input())
    number = input()

    l = list()

    for d in number:
        if l and l[-1] != d:
            l.pop(-1)
        else:
            l.append(d)

    print(len(l))
