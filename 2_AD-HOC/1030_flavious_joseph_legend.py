cases = int(input())

for i in range(cases):
    n, m = map(int, input().strip().split())

    people = list(range(1, n+1))

    index = 0

    while len(people) > 1:
        # Pega o resto da divisão, ou seja, sempre garante que mesmo que a lista diminua, vai deixar o index certinho sem ter que mexer no passo (m+1)
        index = (index + m - 1) % len(people)
        people.pop(index)

    print(f'Case {i + 1}: {people[0]}')