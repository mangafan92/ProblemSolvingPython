nombre = int(input("Nombre:"))

n = str(2**nombre)
s = 0

for k in range(0, len(n)):
    s += int(n[k])
    
print("2 puissance 10000 vaut", n, "et la somme des chiffres qui le compose vaut", s, ".")
