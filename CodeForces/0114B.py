def get_subsets(elements):
    if not elements:
        yield tuple()
    else:
        for subset_rec in get_subsets(elements[1:]):
            yield subset_rec
            yield (elements[0],) + subset_rec


def is_valid_set(subset, pairs):
    subset = set(subset)
    ok = True
    for pair in pairs:
        ok = ok and (not (pair[0] in subset and pair[1] in subset))
    return ok


if __name__ == '__main__':
    n, m = map(int, input().split())
    names = tuple(input() for _ in range(n))
    pairs = [input().split() for _ in range(m)]

    ok = lambda subset: is_valid_set(subset, pairs)
    team = max(filter(ok, get_subsets(names)), key=len)

    print(len(team))
    for name in sorted(team):
        print(name)
