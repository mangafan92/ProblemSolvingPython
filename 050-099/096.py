import itertools

with open("./data/096_sudoku.txt", "r") as file:
    content = file.read()

def isNotInLine(sudoku, number, line):
    return not number in sudoku[line]

def isNotInColumn(sudoku, number, column):
    return not number in [sudoku[k][column] for k in range(9)]

def isNotInSquare(sudoku, number, line, column):
    square = line//3*3, column//3*3
    return not number in [sudoku[i][j] for i, j in itertools.product(range(square[0], square[0]+3), range(square[1], square[1]+3))]

def isPossibleNumber(sudoku, number, line, column):
    return isNotInLine(sudoku, number, line) and isNotInColumn(sudoku, number, column) and isNotInSquare(sudoku, number, line, column)

def isValidSudoku(sudoku, position):
    if position == 81:
        return True

    line = position // 9
    column = position % 9

    if sudoku[line][column] != 0:
        return isValidSudoku(sudoku, position+1)

    for k in range(1, 10):
        if isPossibleNumber(sudoku, k, line, column):
            sudoku[line][column] = k

            if isValidSudoku(sudoku, position+1):
                return True

    sudoku[line][column] = 0
    return False

def contentToSudokus(content):
    content = content.splitlines()
    content = [content[10*k+1:10*k+10] for k in range(len(content)//10)]
    lineToList = lambda line: list(map(list, line))
    content = list(map(lineToList, content))
    lineToInt = lambda line: list(map(int, line))
    sudokuToInt = lambda sudoku: list(map(lineToInt, sudoku))
    content = list(map(sudokuToInt, content))
    return content

def solveProblem(content=content):
    sudoku = contentToSudokus(content)

    for k in range(len(sudoku)):
        isValidSudoku(sudoku[k], 0)

    numbers = [sudoku[k][0][:3] for k in range(len(sudoku))]
    toBase10 = lambda tab: sum([tab[k]*10**(2-k) for k in range(len(tab))])
    numbers = list(map(toBase10, numbers))
    return sum(numbers)

if __name__ == '__main__':
    print(solveProblem())