import sys

keyboard_map = {
    '1': '`', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', 
    '8': '7', '9': '8', '0': '9', '-': '0', '=': '-',
    'Q': '\\', 'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 
    'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O', '[': 'P', ']': '[', '\\': ']',
    'A': ';', 'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G', 
    'J': 'H', 'K': 'J', 'L': 'K', ';': 'L', "'": ';',
    'Z': '/', 'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 
    'M': 'N', ',': 'M', '.': ',', '/': '.'
}

for line in sys.stdin:
    word = list(line)
    new_word = ''

    for letter in word:
        if letter == ' ':
            new_word += ' '
            continue
        elif letter == '\n':
            continue

        new_word += keyboard_map[letter]
    
    print(new_word)