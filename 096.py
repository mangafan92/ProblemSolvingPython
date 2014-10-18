# La technique utilisée pour résoudre les sudokus est expliquées ici: http://fr.openclassrooms.com/informatique/cours/le-backtracking-par-l-exemple-resoudre-un-sudoku

def estValide(sudoku, position):
    if position == 81 :
        return True    
    
    i = position // 9
    j = position % 9
        
    if sudoku[i][j] != 0:
        return estValide(sudoku, position+1)
        
    for k in range(1, 10):
        if absentLigne(sudoku, k, i) and absentColonne(sudoku, k, j) and absentCarre(sudoku, k, i, j):
            sudoku[i][j] = k
            
            if estValide(sudoku, position+1):
                return True
    sudoku[i][j] = 0
    return False
        
def absentLigne(sudoku, nbre, i):
    for k in range(0, 9):
        if sudoku[i][k] == nbre:
            return False
    return True
    
def absentColonne(sudoku, nbre, j):
    for k in range(0, 9):
        if sudoku[k][j] == nbre:
            return False
    return True
    
def absentCarre(sudoku, nbre, i, j):
    for k in range(i-i%3, i-i%3+3):
        for l in range(j-j%3, j-j%3+3):
            if sudoku[k][l] == nbre:
                return False
    return True
    
def isCorrect(sudoku):
    for n in range(0,81):
        # Pour chaque ligne
        for i in range(0, 9):
            # Pour chaque case de la ligne
            for j in range(0, 9):
                if sudoku[i][j] != 0:                
                    # Ligne
                    for k in range(0, 9):
                        if sudoku[i][j] == sudoku[k][j] and k != i:
                            print(i,j,k,j, sudoku[i][j])
                            return False
                    # Colonne
                    for k in range(0, 9):
                        if sudoku[i][j] == sudoku[i][k] and k != j:
                            print(i,j,i,k,sudoku[i][j])
                            return False
                    # Carré de 9 cases
                    for k in range(i-i%3, i-i%3+3):
                        for l in range(j-j%3, j-j%3+3):
                            if sudoku[i][j] == sudoku[k][l] and (k != i and l != j):
                                print(i,j,k,l,sudoku[i][j])                                
                                return False
    return True
                    
    
fichier = open("./données/096_sudoku.txt", "r")
fichier = fichier.read()
fichier = fichier.split()

k = 0

while k < len(fichier):
    if len(fichier[k]) < 5:
        fichier.pop(k)
    else:
        k += 1

for k in range(0, len(fichier)):
    fichier[k] = list(fichier[k])
    
for i in range(0, len(fichier)):
    for j in range(0, len(fichier[i])):
        fichier[i][j] = int(fichier[i][j])
        
sudokus = []

for i in range(0,50):
    sudoku = []
    for j in range(0, 9):
        sudoku.append(fichier[9*i+j])
    sudokus.append(sudoku) 
  
for k in range(0, 50):
    estValide(sudokus[k], 0)
    
#for k in range(0, 50):
#    print(k, isCorrect(sudokus[k]))
#    print("---")

somme = 0

for k in range(0, 50):
    terme = ""    
    for i in range(0, 3):
        terme += str(sudokus[k][0][i])
    somme += int(terme)
        
print("La somme des nombres à 3 chiffres situés en haut à gauche des grilles est", somme, ".")