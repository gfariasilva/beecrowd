import sys

distances = 0
cases = 0

for line in sys.stdin:
    distances += int(input())
    cases += 1

print(round(distances / cases, 1))