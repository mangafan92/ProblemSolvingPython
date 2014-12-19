def anagram(characters, length, repeat = False):
    anagrams = list()
    word = str()
    reorganize(word, characters, length, repeat, anagrams)
    return anagrams

def reorganize(word, characters, length, repeat, anagrams):
    if length > 0:
        for character in characters:
            tmpword = str(word)
            tmpword += str(character)
            if repeat:
                reorganize(tmpword, characters, length-1, repeat, anagrams)
            else:
                tmpchars = list(characters)
                tmpchars.remove(character)
                reorganize(tmpword, tmpchars, length-1, repeat, anagrams)
    else:
        anagrams.append(word)

if __name__ == '__main__':
    # debug
    characters = list(range(0,3))
    print(anagram(characters, len(characters)))