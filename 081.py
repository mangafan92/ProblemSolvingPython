def sommeMin(x, y, matrix, listeSommes): 
    if listeSommes[x][y] == -1:
        if x+1 == len(matrix) and y+1 == len(matrix[x]):
            listeSommes[x][y] = matrix[x][y]
        elif x+1 == len(matrix):
            listeSommes[x][y] = sommeMin(x, y+1, matrix, listeSommes) + matrix[x][y]
        elif y+1 == len(matrix[x]):
            listeSommes[x][y] = sommeMin(x+1, y, matrix, listeSommes) + matrix[x][y]
        else:
            if sommeMin(x+1, y, matrix, listeSommes) < sommeMin(x, y+1, matrix, listeSommes):
                listeSommes[x][y] = sommeMin(x+1, y, matrix, listeSommes) + matrix[x][y]
            else:
                listeSommes[x][y] = sommeMin(x, y+1, matrix, listeSommes) + matrix[x][y]
    return listeSommes[x][y]

fichier = open("./données/081_matrix.txt", "r")
fichier = fichier.read()
fichier = fichier.split()

matrix = []

for k in range(0, 80):
    matrix.append(fichier[k].split(","))
    
for i in range(0, 80):
    for j in range(0, 80):
        matrix[i][j] = int(matrix[i][j])
        
listeSommes = []
for k in range(0, 80):
    listeSommes.append([-1]*80)
    
print("Le chemin dont la somme est minimale a une somme qui vaut", sommeMin(0, 0, matrix, listeSommes),".")