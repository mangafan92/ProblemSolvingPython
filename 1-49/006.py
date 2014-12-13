def sommeDesCarres(n):
    s = 0
    
    for k in range(1,n+1):
        s+=k**2
    
    return s
    
    
def carreDeLaSomme(n):
    s = 0
    
    for k in range(1, n+1):
        s+=k
        
    return s**2
    
n = int(input("Nombre:"))
d = carreDeLaSomme(n)-sommeDesCarres(n)

print("La différence du carré de la somme des nombres allant de 1 à", n, "et de la somme des carrés allant de 1 à", n, "est", d, ".")