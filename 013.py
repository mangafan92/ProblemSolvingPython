fichier = open("./divers/013_numbers.txt", "r")
nombres = fichier.read()
nombres = nombres.split()

s = 0

for k in range(0, len(nombres)):
    s += int(nombres[k])
    
print("Les 10 premiers chiffres de la somme de ces nombres sont", str(s)[0:10], ".")