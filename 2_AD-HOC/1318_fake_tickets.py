import sys

for line in sys.stdin:
    tickets, persons = map(int, line.strip().split())
    if not tickets and not persons:
        exit()
        
    numbers = list(map(int, input().strip().split()))
    reduced_numbers = set(numbers)
    counts = []

    for number in reduced_numbers:
        count = numbers.count(number)
        if count > 1:
            counts.append(numbers.count(number))

    print(len(counts))