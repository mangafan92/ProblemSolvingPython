"""
Principe:
    - a chaque tirage, 2 possibilités:
        - on tire une nouvelle couleur
        - ou pas
    - l'arbre de probabilités a 2**20 feuilles (soit ~10**6), on peut le calculer entièrement avec une fonction récursive
    - une bonne partie de l'arbre n'est d'ailleurs jamais calculée puisqu'on peut s'arrêter lorsque toutes les couleurs ont été tirées
"""


def distinctColors(balls: int, ballsToPick: int, colors: int) -> float:
    ballsPerColor = balls // colors

    def distinctColorsRec(ballsLeftToPick: int, currentDistinctColors: int, ballsLeft: int, ballsDistinctColorLeft: int) -> float:
        if ballsLeftToPick == 0 or ballsDistinctColorLeft == 0:
            return currentDistinctColors
        else:
            output = ballsDistinctColorLeft / ballsLeft * distinctColorsRec(ballsLeftToPick - 1, currentDistinctColors + 1, ballsLeft - 1, ballsDistinctColorLeft - ballsPerColor)
            output += (1 - ballsDistinctColorLeft / ballsLeft) * distinctColorsRec(ballsLeftToPick - 1, currentDistinctColors, ballsLeft - 1, ballsDistinctColorLeft)
            return output

    return distinctColorsRec(ballsToPick - 1, 1, balls - 1, balls - ballsPerColor)


def solve():
    return round(distinctColors(70, 20, 7), 9)


if __name__ == '__main__':
    print(solve())
