try:
    while True:
        x, y = [int(i) for i in input().split()]
        print(abs(x - y))
except EOFError:
    exit()