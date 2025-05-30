try:
    while True:
        n = input()
        cases = input().strip().split()

        print(f'Mary won {cases.count("0")} times and John won {cases.count("1")} times')
        
except EOFError:
    exit()