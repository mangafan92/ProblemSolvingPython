limit = 1000
a = 1
b = 2
output = 0

for k in range(limit):
    a, b = b, 2*b + a
    if len(str(a + b)) > len(str(b)):
        output += 1

print("Le nombre de fractions de la série de", limit, "termes est:", output)