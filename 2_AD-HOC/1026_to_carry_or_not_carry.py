import sys

for line in sys.stdin:
    a, b = map(int, line.strip().split())
    print(a ^ b)  # Bitwise XOR (addition without carry)