# Pour certaines valeurs, il y a plusieurs triplets pythagoriciens qui fonctionnent, par exemple pour nombre=1500

nombre = int(input("Nombre:"))
produits = []
valeursA = []
valeursB = []
valeursC = []

for a in range(1, nombre):
    for b in range (a, nombre):
        c = (a**2 + b**2)**(1/2)       
        if int(c) == c and a + b + c == nombre:
            c = int(c)            
            valeursA.append(a)
            valeursB.append(b)
            valeursC.append(c)
            produits.append(a*b*c)
            
if len(produits) != 0:            
    print("Il existe au moins un triplet un triplet pythagoricien tel que a+b+c =", nombre, ".")
    print("Les valeurs de a, b et c qui fonctionnent ainsi que de leurs produits sont:")
    for k in range(0, len(produits)):
        print("a =", valeursA[k], "b =", valeursB[k], "c =", valeursC[k], "a*b*c =", produits[k])        
else:
    print("Il n'existe pas de triplet pythagoricien tel que a+b+c =", nombre, ".")