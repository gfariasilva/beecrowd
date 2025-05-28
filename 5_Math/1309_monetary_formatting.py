try:
    while True:
        dollars = list(input())
        cents = input()

        length = len(dollars)
        commas = 0

        while length > 3:
            commas += 1
            length -= 3

        steps = 0

        for i in range(3, len(dollars), 3):
            if commas > 0:
                dollars.insert(-i - steps,',')
                commas -= 1
                steps += 1
            else:
                break

        if int(cents) < 10:
            cents = list(cents)
            cents.insert(0, '0')

        print(f"${''.join(dollars)}.{''.join(cents)}")
        
except EOFError:
    exit()