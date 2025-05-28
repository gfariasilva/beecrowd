try:
    while True:
        year = int(input().strip())
        ordinary = True
        leap = False

        if not year % 400 or ((not year % 4) and year % 100):
            print('This is leap year.')
            ordinary = False
            leap = True
        
        if not year % 15:
            print('This is huluculu festival year.')
            ordinary = False

        if not year % 55 and leap:
            print('This is bulukulu festival year.')
            ordinary = False
        
        if ordinary:
            print('This is an ordinary year.')

        print()
        
except EOFError:
    exit()