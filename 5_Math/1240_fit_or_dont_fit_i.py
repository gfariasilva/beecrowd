for _ in range(int(input())):
    a, b = input().split()

    if a[-len(b):] == b:
        print("encaixa")
    else:
        print("nao encaixa")