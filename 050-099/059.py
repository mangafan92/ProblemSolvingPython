import string
import itertools

expectedLettersFrequency = 0.75

with open("./data/059_cipher.txt", "r") as file:
    content = file.read()

def decrypt(table, key):
    table = list(table)
    for k in range(len(table)):
        table[k] ^= key[k%len(key)]
    return table

def toLowercasedChars(message):
    message = list(map(chr, message))
    message = list(map(str.lower, message))
    return message

def lettersFrequency(message):
    frequency = 0
    for letter in string.ascii_lowercase:
        frequency += message.count(letter)/len(message)
    return frequency > expectedLettersFrequency

content = content.split(",")
content = list(map(int, content))

characters = string.ascii_lowercase
characters = list(characters)
characters = list(map(ord, characters))

keys = [list() for k in range(3)]

for modulo in range(3):
    letters = [content[k] for k in range(modulo, len(content), 3)]

    for key in characters:
        message = toLowercasedChars(decrypt(letters, (key,)))
        if lettersFrequency(message):
            keys[modulo].append(key)

for key in itertools.product(*keys):
    print("key: {}, sum: {}, message: {}".format(key, sum(decrypt(content, key)), "".join(toLowercasedChars(decrypt(content, key)))))