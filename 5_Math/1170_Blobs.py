for _ in range(int(input())):
    food = float(input())
    days = 1
    count = days

    while days < food:
        days = days * 2
        count = count + 1
    
    print(f'{count - 1} dias')