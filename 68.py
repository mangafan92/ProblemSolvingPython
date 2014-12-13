def anagram(characters, length, repeat = False):
    anagrams = list()
    word = str()
    reorganize(word, characters, length, repeat, anagrams)
    return anagrams

def reorganize(word, characters, length, repeat, anagrams):
    if length > 0:
        for character in characters:
            tmpword = str(word)
            tmpword += " " +str(character)
            if repeat:
                reorganize(tmpword, characters, length-1, repeat, anagrams)
            else:
                tmpchars = list(characters)
                tmpchars.remove(character)
                reorganize(tmpword, tmpchars, length-1, repeat, anagrams)
    else:
        word = word.strip(" ")
        permutation = correctpermutation(word)
        if permutation[0]:
            anagrams.append(permutation[1])

def correctpermutation(word):
    word = word.split(" ")
    sums = list()
    sequence = list()

    for k in range(len(word)//2-1, -1, -1):
        ids = []

        ids.append(k)
        ids.append( (k+1)%(len(word)//2) )
        ids.append( (k+1)%(len(word)//2) + len(word)//2 )

        ids.reverse()

        sumtmp = 0
        stringtmp = ""

        for id in ids:
            sumtmp += int(word[id])
            stringtmp += word[id]
        sums.append(sumtmp)
        sequence.append(int(stringtmp))

    for sum1 in sums:
        for sum2 in sums:
            if sum1 != sum2:
                return False, None

    sequence = sortsequence(sequence)

    return True, sequence

def sortsequence(sequence):
    tmpsequence = []

    p = sequence.index(min(sequence))

    # print(min(sequence))

    for k in range(len(sequence)):
        tmpsequence.append(sequence[(k+p)%len(sequence)])

    return tmpsequence

if __name__ == '__main__':
    characters = list(range(1,11))
    permutations = anagram(characters, len(characters))

    for k in range(len(permutations)):
        for i in range(len(permutations[k])):
            permutations[k][i] = str(permutations[k][i])
        permutations[k] = int("".join(permutations[k]))

    while max(permutations) > 10**16:
        permutations.remove(max(permutations))

    print("La plus grande chaîne est:", max(permutations))