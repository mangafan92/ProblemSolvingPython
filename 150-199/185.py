with open("./data/185_guesses.txt", "r") as file:
    content = file.read()

def isCoherentWithGuesses(sequence, guesses):
    for guess in guesses:
        corrects = 0
        for k in range(len(sequence)):
            if sequence[k] == guess[0][k]:
                corrects += 1
        if (sequence[-1] != "-1" and corrects != guess[1]) or (corrects > guess[1]):
            return False

    return True

def isValidSequence(sequence, guesses, position):
    print(sequence)
    if position==len(sequence):
        return True

    for k in map(str, range(10)):
        sequence[position] = k

        if isCoherentWithGuesses(sequence, guesses) and isValidSequence(sequence, guesses, position+1):
            return True

    sequence[position] = "-1"
    return False

def contentToGuesses(content):
    content = content.splitlines()
    eraseUselsess = lambda line: line.replace("correct", "").replace(";", "")
    content = list(map(eraseUselsess, content))
    content = list(map(lambda line: line.split(" "), content))
    content = list(map(lambda line: (line[0], int(line[1])), content))
    content = list(sorted(content, key=lambda guess: guess[1]))
    return content

def solveProblem(content=content):
    guesses = contentToGuesses(content)

    sequence = ["-1"]*len(guesses[0][0])

    isValidSequence(sequence, guesses, 0)

    return int("".join(sequence))

if __name__ == '__main__':
    print(solveProblem())