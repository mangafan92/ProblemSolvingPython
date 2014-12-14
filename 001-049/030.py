def sommeDigitsPuissance(nombre, puissance):
    nombre = str(nombre)
    somme = 0
    for digit in nombre:
        somme += int(digit)**puissance
    return somme
    
def maximumSomme(puissance):
    s = "9"
    while int(s) < sommeDigitsPuissance(int(s), puissance):
        s += "9"
    return int(s)

somme = 0
puissance = int(input("Nombre:"))

for k in range(2, maximumSomme(puissance)):
    if k == sommeDigitsPuissance(k, puissance):
        somme += k
        
print("La somme des nombres étant la somme de leur digits élevés à la puissance", puissance, "est", somme, ".")