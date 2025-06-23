import sys

for line in sys.stdin:
    desired, current = int(line), int(input())
    print(desired-current)