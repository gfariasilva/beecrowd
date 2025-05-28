import sys

for line in sys.stdin:
    for i in range(int(line)):
        case = list(input().strip())
        a = int(case[0])
        b = int(case[2])

        if a == b:
            print(a * b)
        elif case[1].islower():
            print(a + b)
        else:
            print(b - a)