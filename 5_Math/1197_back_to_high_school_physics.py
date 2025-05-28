try:
    while True:
        x, y = [int(i) for i in input().split()]

        print(x * y * 2)
except EOFError:
    exit()