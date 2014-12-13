def mini(table):
    mini = -1
    for k in range(0, len(table)):
        if table[k] < mini or mini == -1:
            mini = table[k]
    return mini
    
def sommeColonne(colonne, debut, fin, table):
    s = 0
    if debut == fin:
        s = table[debut][colonne]
    elif debut < fin:
        for k in range(debut, fin+1):
            s += table[k][colonne]
    elif debut > fin:
        for k in range(fin, debut+1):
            s += table[k][colonne]
    return s

fichier = open("./data/081_matrix.txt", "r")
fichier = fichier.read()
fichier = fichier.split()

matrix = []

for k in range(0, 80):
    matrix.append(fichier[k].split(","))
    
for i in range(0, 80):
    for j in range(0, 80):
        matrix[i][j] = int(matrix[i][j])

sommesMin = []

for k in range(0,80):
    sommesMin.append(80*[-1])

for k in range(0,80):
    sommesMin[k][0] = matrix[k][0]
    
for i in range(1, 80):
    for j in range(0, 80):
        listeSommes = []
        for k in range(0,80):
            listeSommes.append(sommeColonne(i, j, k, matrix) + sommesMin[k][i-1])
        sommesMin[j][i] = mini(listeSommes)

sommesFinales = []

for k in range(0, 80):
    sommesFinales.append(sommesMin[k][79])
    
print("La somme minimale est", mini(sommesFinales), ".")