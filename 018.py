def moyenneColonne(x, y, table):
    diviseur = 0
    sommePonderee = 0
    
    for k in range(x+1, len(table)):        
        coef = len(table) - k
        diviseur += coef
        sommePonderee += coef*int(table[k][y])
        
    return sommePonderee / diviseur

def moyenneDiagonale(x, y, table):
    diviseur = 0
    sommePonderee = 0
#    print("depart", x, y, len(table)-x)    
    for k in range(0, len(table)-x):        
        coef = len(table) - k
        diviseur += coef
        sommePonderee += coef*int(table[x+k][y+k]) 
        
#        print("div", diviseur, "somme", sommePonderee)
#        print(k, y+k, len(table[k])) 

    print("somme finale", sommePonderee, "diviseur final", diviseur)
    out = sommePonderee / diviseur
    return out

pyramideStr = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
pyramideStr = pyramideStr.split()

# On stocke les nombres de pyramideStr[] dans un tableau où chaque ligne possède une case de plus que la précédente
# La première ligne est composée de la case [0][0], la 2ème des cases [1][0] et [1][1] etc
pyramide = []
pos = 0
k= 0

while pos <= len(pyramideStr):  
    pyramide.append(pyramideStr[pos-k:pos])
    k += 1    
    pos += k
        
pyramide.pop(0)

#L'algorithme en lui-même commence

a = 0
b = 0
s = int(pyramide[0][0])

while a < len(pyramide)-1:
    # A chaque étape, on peut aller soit vers le bas, soit vers le bas et vers la droite (en diagonale)
    # On compare donc les moyennes pondérées de la ligne et de la colonne dont on va potentiellement devoir se priver pour la suite en choisissant la case suivante
    # Et, évidemment, on se prive de celle qui à la moyenne pondérée la plus faible 
    # (plus un nombre est éloigné de la case où ou es, moins il est important dans le calcul de moyenne)
    
    colonne = moyenneColonne(a,b, pyramide)
    diagonale = moyenneDiagonale(a,b, pyramide)    
    
    if colonne > diagonale:
        a += 1
        s += int(pyramide[a][b])
    else:
        a += 1
        b += 1
        s += int(pyramide[a][b])
    
    print("Case", a, b)    
    print("Somme intemédiaire", s)
        
print(s)