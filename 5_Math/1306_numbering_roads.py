cases = 0

while True:
    r, n = [int(i) for i in input().split()]
    cases += 1

    if not r and not n:
        exit()

    condition = r - n 

    if condition <= 0:
        print(f'Case {cases}: 0')
    elif condition > 26 * n:
        print(f'Case {cases}: impossible')
    else:
        result = 0
        for i in range(26):
            if condition - (i * n) > 0:
                continue
            else:
                result = i
                break
        print(f'Case {cases}: {result}')