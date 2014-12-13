nombre = int(input("Nombre:"))
s = 0

for k in range(1, nombre+1):
    s += k**k
    s %= 10**10
    
print("Les 10 derniers chiffres de la somme des nombres allant de 1^1 à", nombre, "^", nombre, "sont", s, ".")