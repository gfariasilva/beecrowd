while True:
    x1, y1, x2, y2 = map(int, input().strip().split())

    if not x1 and not y1 and not x2 and not y2:
        break

    queen = [x1, y1]
    position = [x2, y2]

    moves = 0

    if position != queen:
        diag_1 = []
        diag_2 = []
        times = 0

        for i in range(x1+1, 9):
            times += 1
            if y1 + times <= 8:
                diag_1.append([i, y1+times])
            if y1 - times:
                diag_2.append([i, y1-times])
        times = 0
        for i in range(x1-1,0,-1):
            times += 1
            if y1 - times:
                diag_1.append([i, y1-times])
            if y1 + times <= 8:
                diag_2.append([i, y1+times])

        if position[0] == queen[0] or position[1] == queen[1] or position in diag_1 or position in diag_2:
            moves = 1
        else:
            moves = 2

    print(moves)