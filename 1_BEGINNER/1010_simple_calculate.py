import sys

for line in sys.stdin:
    t1 = list(line.strip().split())
    c1, n1 = map(int, [t1[0], t1[1]])
    p1 = float(t1[2])
    t2 = list(input().strip().split())
    c2, n2 = map(int, [t2[0], t2[1]])
    p2 = float(t2[2])

    print(f'VALOR A PAGAR: R$ {p1 * n1 + p2 * n2:.2f}')