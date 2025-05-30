import sys

for line in sys.stdin:
    n, d = map(int, line.strip().split())
    if not n and not d:
        exit()
    
    totals = [0 for i in range(n)]

    for dinner in range(d):
        alumni = list(map(int, input().strip().split()))
        totals = [total + alumn for total, alumn in zip(totals, alumni)]

    print('yes' if d in totals else 'no')