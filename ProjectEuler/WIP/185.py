with open("./data/185_guesses.txt", "r") as file:
    content = file.read()

elementsSorted = dict()

def elementsSortedByLikeliness(guesses, position):
    try:
        return elementsSorted[position]
    except:
        elements = {str(k): 0 for k in range(10)}
        for guess in guesses:
            elements[guess[0][position]] += guess[1]

        print(elements)
        elementsSorted[position] = list(reversed(sorted(elements.keys(), key=lambda value: elements[value])))
        return elementsSorted[position]

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

    for k in elementsSortedByLikeliness(guesses, position):
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