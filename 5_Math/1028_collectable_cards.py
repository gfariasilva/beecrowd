cases = int(input())

outputs = []

if 1 <= cases <= 3000:
    for _ in range(0, cases):
        numbers = [int(i) for i in input().strip().split(' ')]
        numbers_sorted = sorted(numbers)

        n = numbers_sorted[0]

        while True:
            if numbers[1] == 0:
                print(numbers[0])
                break
            elif ((not numbers[0] % n) and (not numbers[1] % n)):
                print(n)
                break
            else:
                n -= 1