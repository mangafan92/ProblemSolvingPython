fichier = open("./divers/011_grid.txt", "r")

nombres = fichier.read()
nombres = nombres.split()

# Déclaration d'une liste de 20 éléments qui contient des listes de 20 éléments afin de modéliser la grille de 20x20
grid = []
for k in range(0,20):
    grid.append([0]*20)

# On remplis le tableau avec les nombres de la chaîne
for k in range(0, 20):
    for j in range(0, 20):
        grid[k][j] = int(nombres[k*20+j])

nombre =  int(input("Nombre:"))
produit = 0

# Lignes
for i in range(0,20):    
    for j in range(0,20-nombre):
        produitTemp = 1
        
        for k in range(j, j+nombre):
            produitTemp *= grid[i][k]

        if produitTemp > produit:
            produit = produitTemp
# Colonnes          
for i in range(0,20):    
    for j in range(0,20-nombre):
        produitTemp = 1
        
        for k in range(j, j+nombre):
            produitTemp *= grid[k][i]

        if produitTemp > produit:
            produit = produitTemp
    
# Diagonales allant de la gauche vers la droite et du bas vers le haut
for i in range(nombre, 20):
    for j in range(0, 20-nombre):
        produitTemp = 1
        
        for k in range(0, nombre):
            produitTemp *= grid[i-k][j+k]
            
        if produitTemp > produit:
            produit = produitTemp
    
# Diagonales allant de la gauche vers la droite et du haut vers le bas
for i in range(0, 20-nombre):
    for j in range(0, 20-nombre):
        produitTemp = 1
        
        for k in range(0, nombre):
            produitTemp *= grid[i+k][j+k]
            
        if produitTemp > produit:
            produit = produitTemp
            
print("Le plus grand produits de", nombre, "nombres aligné(s) en ligne, colonne ou diagonale de la grille est", produit, ".")