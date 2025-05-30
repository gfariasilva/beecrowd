import sys

for line in sys.stdin:
    a, b = map(int, line.strip().split())
    count = 0

    for i in range(a, b+1):
        no_repeated = set(list(str(i)))
        count += 1 if len(no_repeated) == len(list(str(i))) else 0

    print(count)