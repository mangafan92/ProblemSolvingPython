def factorielle(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorielle(n-1)

def sommeFactoriellesDigits(n):
    s = 0
    n = str(n)
    for k in range(0, len(n)):
        s += factorielle(int(n[k]))
    return s
        
s = 0

for k in range(3, 1000000):
    if k == sommeFactoriellesDigits(k):
        print(k, sommeFactoriellesDigits(k))
        s += k

print(s)