numbers = {}

for i in range(int(input())):
    n = int(input().strip())
    if n not in numbers:
        numbers[n] = 1
    else:
        numbers[n] += 1

sorted_dict = dict(sorted(numbers.items()))

for key, value in sorted_dict.items():
    print(f'{key} aparece {value} vez(es)')