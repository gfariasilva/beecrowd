import sys

cases = 0

for line in sys.stdin:
    cases += 1
    shoe = line.strip()
    box = sys.stdin.readline().strip().split()

    m = 0
    f = 0

    while shoe in box:
        i = box.index(shoe)

        if box[i+1] == 'M':
            m += 1
        else:
            f += 1

        box.pop(i)

    if cases >= 2:
        print()
        
    print(f'Caso {cases}:')
    print(f'Pares Iguais: {m + f}')
    print(f'F: {f}')
    print(f'M: {m}')