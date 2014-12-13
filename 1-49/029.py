liste = []

borne = int(input("Nombre:"))

for i in range(2, borne+1):
    for j in range(2, borne+1):
        n = i**j
        if not n in liste:
            liste.append(n)
            
print("La liste comporte", len(liste), "termes.")