import string
import math

squares = [x**2 for x in range(10000)]
squaresLen = {x: list() for x in range(1, 15)}

for square in squares:
    try:
        squaresLen[math.floor(math.log10(square))+1].append(square)
    except:
        squaresLen[1].append(square)

with open("./data/098_words.txt", "r") as file:
    words = file.read()
    words = words.split(",")
    words = list(map(lambda n: n.strip("\""), words))
    words = list(map(str.lower, words))

sortedWords = list(map(lambda word: "".join(sorted(word)), words))

anagrams = list()

for k in range(len(words)):
    if sortedWords.count(sortedWords[k]) > 1:
        anagrams.append(words[k])

sortedAnagrams = list(map(lambda word: "".join(sorted(word)), anagrams))

couples = set()

for i in range(len(sortedAnagrams)):
    for j in range(len(sortedAnagrams)):
        if sortedAnagrams[i] == sortedAnagrams[j] and i != j:
            couples.add(tuple(sorted((anagrams[i], anagrams[j]))))

greatest = 0

for couple in couples:
    for square in squaresLen[len(couple[0])]:
        conversionTable = {couple[0][x]: str(square)[x] for x in range(len(couple[0]))}

        if len(list(set(conversionTable.values()))) != len(conversionTable):
            continue

        convertLetter = lambda letter: conversionTable[letter]
        convert = lambda word: int("".join(map(convertLetter, list(word))))

        squareCouple = [convert(word) for word in couple]
        # print(couple, squareCouple)

        if squareCouple[1] in squaresLen[len(couple[0])] and max(squareCouple) > greatest:
            greatest = max(squareCouple)

print(greatest)