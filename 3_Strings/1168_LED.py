leds = [6,2,5,5,4,5,6,3,7,6]

cases = int(input())

for _ in range(cases):
    total = 0

    number = [int(i) for i in list(input())]
    result = 0

    for n in number:
        result += leds[n]

    print(f'{result} leds')