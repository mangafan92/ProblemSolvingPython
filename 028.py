from time import time

def sommeSpirale(n):
    somme = 1
    dernierChiffre = 1
    borne = (n-1)//2 # Cela correspond au nombre de "carrés" dont il faudra additionner les coins, on ne compte pas le centre
    
    # Pour chaque carré    
    for k in range(0, borne):
        # Pour chaque coin du carré
        for i in range(0, 4):
            dernierChiffre += 2*k+2
            somme += dernierChiffre
            
    return somme
    
nombre = int(input("Nombre impair:"))

debut = time()   
    
print("\nLa somme des nombres sur les diagonales d'une spirale de {} par {} vaut {}.".format(nombre, nombre, sommeSpirale(nombre)))

print("\nL'algorithme a mis {}s à s'exécuter.".format(round(time()-debut, 2)))