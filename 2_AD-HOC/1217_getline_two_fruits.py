import sys

for line in sys.stdin:
    prices = 0
    kgs = 0

    for i in range(int(line)):
        prices += float(input())
        names = input().strip().split()
        kgs += len(names)

        print(f'day {i+1}: {len(names)} kg')

    print(f'{round(kgs / int(line), 2)} kg by day')
    print(f'R$ {round(prices / int(line), 2)} by day')