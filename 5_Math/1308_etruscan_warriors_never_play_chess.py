try:
    while True:
        n = int(input())
        steps = 0

        for i in range(1,n):
            if n <= 0 or n < i:
                break
            
            n -= i
            steps += 1

        print(steps)
        
except EOFError:
    exit()