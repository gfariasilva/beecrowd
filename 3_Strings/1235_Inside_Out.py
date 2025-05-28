cases = int(input())

for _ in range(cases):
    text = list(input())
    half = int(len(text) / 2)

    first = text[:half]
    last = text[half:]

    print(*(first[::-1] + last[::-1]), sep='')