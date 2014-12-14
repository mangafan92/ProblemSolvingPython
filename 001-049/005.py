def estDivisible(N, n1, n2):
    for k in range(n1, n2+1):
        if N%k != 0:
            return False;
            
    return True

def estPremier(n):
    for k in range(2, int(n**(1/2))+1):
        if n % k == 0:
            return False
    return True

def produitNombrePremiersEntre(n1, n2):
    p = 1
    for k in range(n1, n2+1):
        if estPremier(k):
            p*=k
    return p

borne = int(input("Nombre:"))
k = 0
p = produitNombrePremiersEntre(1,borne)

while not estDivisible(k, 1, borne) or k == 0:
    k += p
    
print("Le plus petit nombre divisible par tous les entiers compris entre 1 et", borne, "est", k, ".")

# Le produit des nombres premier compris entre 1 et borne divise forcément un nombre divisible par tous les entiers compris entre 1 et borne 
# On peut donc directement tester tout les entiers de la forme k*p
    