from math import log

fichier = open("./données/099_base_exp.txt", "r")

liste = fichier.read()
liste = liste.splitlines()

for k in range(0, len(liste)):
    liste[k] = liste[k].split(",")

ligne = 0
nombres = [0]*len(liste)

for k in range(0, len(liste)):
    nombres[k] = int(liste[k][1]) * log(int(liste[k][0]))
    if nombres[k] > nombres[ligne]:
        ligne = k

print("La ligne qui possède la plus grande valeur numérique est la ligne", ligne+1, ".")
