while True:
    queries = int(input())

    if not queries:
        break

    n, m = map(int, input().strip().split())
    
    for i in range(queries):
        x, y = map(int, input().strip().split())

        if x == n or y == m:
            print('divisa')
        elif x < n:
            if y > m:
                print('NO')
            else:
                print('SO')
        else:
            if y > m:
                print('NE')
            else:
                print('SE')