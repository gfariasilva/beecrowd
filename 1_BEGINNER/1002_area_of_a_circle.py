import sys

for line in sys.stdin:
    a = float(line) * float(line) * 3.14159
    print(f'A={a:.4f}')