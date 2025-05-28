while True:
    cases = int(input())

    if not cases:
        break

    for i in range(cases):
        questions = list(map(int, input().strip().split()))
        alternatives = ['A', 'B', 'C', 'D', 'E']

        marked = list(map(lambda x: x <= 127, questions))
        n = marked.count(True)

        if n > 1 or n < 1:
            print('*')
        else:
            print(alternatives[marked.index(True)])