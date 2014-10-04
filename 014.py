def nombreTermesSequenceCollatz(n):
    k = 1
    while n != 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n+1
        k += 1
    return k

borne = int(input("Nombre:"))
nombreDepart = 1
nombreTermes = 1
        
for k in range(1, borne+11000):
    temp = nombreTermesSequenceCollatz(k)
    if temp > nombreTermes:
        nombreDepart = k
        nombreTermes = temp
        
print("Le nombre de départ inférieur à", borne,"qui déclenche la séquence la plus longue est", nombreDepart, "et la séquence possède", nombreTermes, "termes.")