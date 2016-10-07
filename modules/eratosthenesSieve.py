def primes(limit: int):
    l = [True for k in range(limit)]

    for i in range(2, limit):
        if l[i] == True:
            for j in range(i ** 2, limit, i):
                l[j] = False
            yield i
