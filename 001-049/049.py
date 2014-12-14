from time import time

def genererListeNombresPremiers(borne):
    liste = [2]
    for k in range(3, borne+1):
        if estPremier(k, liste):
            liste.append(k)
    return liste
                
def estPremier(nombre, liste):
    for k in range(0, len(liste)):
        if nombre % liste[k] == 0:
            return False
    return True
    
def annagramme(a, b):
    a = str(a)
    b = str(b)
    
    if len(a) != len(b):
        return False
        
    for k in range(len(a)):
        if not a[k] in b:
            return False
            
    for k in range(len(b)):
        if not b[k] in a:
            return False
            
    return True

liste = genererListeNombresPremiers(10000)

debut = time()

while liste[0] < 1000:   
    liste.pop(0)

print("Les triplets de nombres premiers inférieurs à 10000 et vérifiant la propriété sont:")

for i in range(len(liste)):
    for j in range(i+1, len(liste)):
        if (2*liste[j] - liste[i]) in liste and annagramme(liste[i], liste[j]) and annagramme(liste[i], 2*liste[j] - liste[i]):
            print("({}, {}, {})".format(liste[i], liste[j], 2*liste[j] - liste[i]))
            
print("\nL'algorithme a mis {}s à s'exécuter.".format(round(time()-debut, 2)))