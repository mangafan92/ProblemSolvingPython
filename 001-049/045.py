def hexagonal(n):
    return int(n*(2*n-1))
    
def pentagonal(n):
    return int(n*(3*n-1)/2)

def triangulaire(n):
    return int(n*(n+1)/2)
    
listePentagonals = []
listeHexagonals = []

nombre = int(input("Nombre:"))

print("Les nombres triangulaires, pentagonaux et hexagonaux inférieurs à triangulaire(", nombre, ") = ", triangulaire(nombre), "sont:")

for k in range(1, nombre):
    listePentagonals.append(pentagonal(k))
    listeHexagonals.append(hexagonal(k))
    
    if triangulaire(k) in listePentagonals and triangulaire(k) in listeHexagonals:
        print(triangulaire(k))