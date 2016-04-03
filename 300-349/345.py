"""
Principe:
    - la somme de la matrice m peut se calculer récursivement
        - elle vaut max(m[0][k] + sommeMatrice(sousMatrice(0, k))) où sousMatrice(0, k)) est la sous-matrice de m qu'on obtient en supprimant la ligne 0 et la colonne k
        - on stocke en mémoire les sommes des sous-matrices mises en jeu durant les appels récursifs pour éviter de les calculer plusieurs fois
"""


def matrixSum(matrix: list) -> int:
    """
    :param matrix: matrice carrée dont on veut calculer la somme, sous forme de liste de listes
    :return: somme de la matrice (du même type que les coefficient de la matrice)
    """
    results = dict()  # pour stocker les sommes de sous-matrices en mémoire

    def matrixSumRec(left: tuple) -> int:
        """
        :param left: tuple contenant les indices et colonnes restantes dans la sous-matrice qu'on étudie (on sait qu'on enlève les lignes dans l'ordre, pas besoin d'avoir une liste pour stocker les lignes restantes)
        :return: somme de la sous-matrice décrite par left
        """
        if len(left) == 0:
            return 0  # [] décrit la sous-matrice de taille 0x0
        else:
            try:
                return results[left]  # pas besoin de le recalculer si on l'a déjà calculé avant
            except:
                l = len(matrix) - len(left)  # indice de la ligne qu'on va enlever à cette étape
                nextMatrix = lambda k: tuple(i for i in left if not i == k)  # renvoie le tableau décrivant la sous-matrice obtenue quand on enlève la colonne k et la ligne l
                results[left] = max(matrix[l][k] + matrixSumRec(nextMatrix(k)) for k in left)  # on stocke le résultat en mémoire
                return results[left]

    left = tuple(range(0, len(matrix)))
    return matrixSumRec(left)


def stringToMatrix(s: str) -> list:
    """
    :param s: string issu du fichier où est stocké la matrice
    :return: liste qu'on peut envoyer à la fonction matrixSum
    """
    matrix = s.replace(" " * 3, " ").replace(" " * 2, " ")
    matrix = matrix.splitlines()
    matrix = [line.strip().split(" ") for line in matrix]
    matrix = [list(map(int, line)) for line in matrix]
    return matrix


def solve():
    return matrixSum(stringToMatrix(open("./data/345_matrix.txt", "r").read()))


if __name__ == '__main__':
    print(solve())
