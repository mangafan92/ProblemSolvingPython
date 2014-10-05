# Ce fichier est une copie de 018.py puisque les problèmes 018 et 067 sont le même problème
# Le seul changement effectué est celui du changement de l'emplacement du fichier

def somme(a,b, pyramide, table):
    if table[a][b] == 0: 
        if len(pyramide)-1 == a:
            return int(pyramide[a][b])
        else:
            somme1 = somme(a+1,b, pyramide, table)
            somme2 = somme(a+1,b+1, pyramide, table)
            if somme1 > somme2:
                table[a][b] = int(pyramide[a][b]) + somme1                
            else:
                table[a][b] = int(pyramide[a][b]) + somme2
    return table[a][b]

fichier = open("./données/067_triangle.txt", "r")    
    
pyramideStr = fichier.read()
pyramideStr = pyramideStr.split()

pyramide = []
table = []
pos = 0
k= 0

while pos <= len(pyramideStr):  
    pyramide.append(pyramideStr[pos-k:pos])
    table.append([0]*(k+1))
    k += 1    
    pos += k
        
pyramide.pop(0)

print(somme(0, 0, pyramide, table))

