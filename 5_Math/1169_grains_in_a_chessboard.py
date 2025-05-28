for _ in range(int(input())):
    squares = int(input())
    grains = 1

    for _ in range(squares):
        grains *= 2

    print(f'{int(grains/12000)} kg')