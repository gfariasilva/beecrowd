def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

try:
    while True:
        m, n = [int(i) for i in input().split()]

        print(factorial(m) + factorial(n))
except EOFError:
    exit()