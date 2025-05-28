from math import sqrt

for _ in range(int(input())):
    x = int(input())

    prime = True if x > 1 else False

    for i in range(2,int(sqrt(x))+1):
        if not (x % i):
            prime = False
            break
    
    print('Prime') if prime else print('Not Prime')