import string

if __name__ == '__main__':
    characters = string.ascii_lowercase
    rank = {char: k for k, char in enumerate(characters)}

    word = input()
    current_char = "a"
    moves = 0

    for char in word:
        moves += min(abs(rank[char] - rank[current_char]), 26 - abs(rank[char] - rank[current_char]))
        current_char = char

    print(moves)
