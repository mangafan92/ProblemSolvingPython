def distinctColors(balls:int, ballsToPick: int, colors:int):
    ballsPerColor = balls//colors

    def distinctColorsRec(ballsLeftToPick: int, currentDistinctColors: int, ballsLeft: int, ballsDistinctColorLeft: int):
        if ballsLeftToPick == 0 or ballsDistinctColorLeft == 0:
            return currentDistinctColors
        else:
            output = ballsDistinctColorLeft/ballsLeft*distinctColorsRec(ballsLeftToPick-1, currentDistinctColors+1, ballsLeft-1, ballsDistinctColorLeft-ballsPerColor)
            output += (1 - ballsDistinctColorLeft/ballsLeft)*distinctColorsRec(ballsLeftToPick-1, currentDistinctColors, ballsLeft-1, ballsDistinctColorLeft)
            return output

    return distinctColorsRec(ballsToPick-1, 1, balls-1, balls-ballsPerColor)

def solve():
    return round(distinctColors(70, 20, 7),9)

if __name__ == '__main__':
    print(solve())