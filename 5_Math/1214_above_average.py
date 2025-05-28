for _ in range(int(input())):
    average_case = list(map(int, input().split()))

    qtd = average_case[0]
    grades = average_case[1:]

    average = sum(grades)/qtd

    count = 0

    for grade in grades:
        if grade > average:
            count += 1

    print(f"{count/qtd * 100:.3f}%")