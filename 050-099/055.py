def estUnNombreDeLychrel(n):
    n = n + int(str(n)[::-1])
    k = 1
    while n != int(str(n)[::-1]):
        n = n + int(str(n)[::-1])
        k += 1
        if k > 50:
            return True
    return False

n = 0
borne = int(input("Nombre:"))

for k in range(1, borne+1):
    if estUnNombreDeLychrel(k):       
        n += 1
print("Il y a", n, "nombre de Lychrel inférieurs à", borne, ".")