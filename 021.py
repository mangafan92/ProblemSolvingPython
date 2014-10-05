def listeDiviseurs(n):
    liste = []
    for k in range(1, n):
        if n % k == 0:
            liste.append(k)
            
    return liste
    
def sommeDiviseurs(n, table):
    if table[n] == 0:    
        liste = listeDiviseurs(n)
        s = 0
        for k in range(0, len(liste)):
            s += liste[k]
        table[n] = s
    return table[n]
            
nombre = int(input("Nombre:"))
listeNombresAmicaux = []
tableSommeDiviseurs = [0] * (nombre+1)

for i in range(1, nombre+1):
    for j in range(i+1, nombre+1):
        if sommeDiviseurs(i, tableSommeDiviseurs) == j and sommeDiviseurs(j, tableSommeDiviseurs) == i:         
            listeNombresAmicaux.append(i)                
            listeNombresAmicaux.append(j)

s = 0

for k in range(0, len(listeNombresAmicaux)):
    s += listeNombresAmicaux[k]
    
print("La somme des nombres amicaux inférieurs à", nombre, "vaut", s, ".")            