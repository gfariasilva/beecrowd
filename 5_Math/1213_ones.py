try:
    while True:
        x = int(input())
        sequence = 11
        length = 2

        while sequence % x:
            sequence = (sequence * 10 + 1) % x
            length += 1

        print(length)
except EOFError:
    exit()