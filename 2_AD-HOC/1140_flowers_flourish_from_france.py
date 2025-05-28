while True:
    sentence = list(map(lambda x: x.lower(), input().strip().split()))

    if sentence == ['*']:
        break

    letters = set()

    for word in sentence:
        letters.add(word[0])

    if len(letters) > 1:
        print('N')
    else:
        print('Y')