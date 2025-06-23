import sys

for line in sys.stdin:
    x, y = map(float, line.split())

    if not x and not y:
        print('Origem')
    elif not x:
        print('Eixo Y')
    elif not y:
        print('Eixo X')
    elif x > 0:
        if y > 0:
            print('Q1')
        else:
            print('Q4')
    else:
        if y > 0:
            print('Q2')
        else:
            print('Q3')