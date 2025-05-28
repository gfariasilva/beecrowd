while True:
    x, y = [list(map(int, j)) for j in [i for i in input().split()]]

    if not int("".join([str(i) for i in x])) and not int("".join([str(i) for i in y])):
        exit()

    operations = 0
    operations_in_this = 0

    x.reverse()
    y.reverse()

    if len(x) < len(y):
        x.extend([0 for _ in range(len(y) - len(x))])
    elif len(x) > len(y):
        y.extend([0 for _ in range(len(x) - len(y))])

    for i, n in enumerate(x):
        sum_digits = n + y[i] + operations_in_this
        if sum_digits >= 10:
            operations += 1
            operations_in_this = 1
        else:
            operations_in_this = 0

    print(f'{operations} carry operation.') if operations == 1 else print(f'{operations} carry operations.') if operations > 0 else print('No carry operation.')