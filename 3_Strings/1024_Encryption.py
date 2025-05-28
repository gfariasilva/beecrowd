cases = int(input())

for _ in range(cases):
    text = input()
    text2 = []

    for i, char in enumerate(text):
        if char.isalpha():
            text2.append(chr(ord(char) + 3))
        else:
            text2.append(char)

    text2 = text2[::-1]

    half = int(len(text2) / 2)

    for i in range(half, len(text2)):
        text2[i] = chr(ord(text2[i]) - 1)

    print(*text2, sep='')