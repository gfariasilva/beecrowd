import math

try:
    while True:
        a, b, c = [int(i) for i in input().split()]

        c1 = math.pi * pow(((a+b-c)/2),2)
        tri = ((a * b) / 2) - c1
        c2 = math.pi * pow(c/2,2) - ((a * b) / 2)

        print(f'{round(c2,4)} {round(tri,4)} {round(c1,4)}')

except EOFError:
    exit()