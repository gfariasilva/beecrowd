import math

try:
    while True:
        d, vf, vg = [int(i) for i in input().split()]

        vf2 = 12 / vf
        vg2 = math.sqrt(pow(d,2) + 144) / vg

        if vg2 <= vf2:
            print('S')
        else:
            print('N')
except EOFError:
    exit()