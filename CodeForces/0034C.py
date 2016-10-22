if __name__ == '__main__':
    pages = list(sorted(set(map(int, input().split(",")))))

    intervals = [[pages[0]]]
    pages.pop(0)

    while pages:
        while pages and intervals[-1][-1] + 1 == pages[0]:
            intervals[-1].append(pages.pop(0))

        if pages:
            intervals.append([pages.pop(0)])

    for i, interval in enumerate(intervals):
        if len(interval) == 1:
            print(interval[0], end="")
        else:
            print("{}-{}".format(interval[0], interval[-1]), end="")
        if i < len(intervals) - 1:
            print(",", end="")
