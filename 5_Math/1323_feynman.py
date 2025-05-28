while True:
    n = int(input())
    if not n:
        exit()
    elif n == 1:
        print(1)
        continue
    
    total = pow(n,2) + 1
    
    for i in range(2, n):
        total += pow((n - i) + 1,2)

    print(total)